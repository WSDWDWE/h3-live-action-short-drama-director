#!/usr/bin/env python3
"""Mechanical checks for an H3 nine-column XLSX; standard library only.

Usage: validate_storyboard.py --xlsx storyboard.xlsx
       [--dialogue-json original_dialogue.json] [--plan-json group_plan.json]

Dialogue JSON: [{"speaker_id": "S1", "text": "原句。"}, ...], or a list
of strings (which checks only the complete dialogue text, not speakers).
Plan JSON: [{"seq": 1, "mode": "ordinary", "state_changes": [...]}, ...].
This checks prompt text, not generated video, speech, or semantic quality.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile


HEADERS = ["剧本名", "分镜序号", *[f"参考图{i}" for i in range(1, 6)],
           "继承上一镜尾帧", "提示词"]
FIELDS = ["subject_definitions", "summary", "retention_analysis",
          "detailed_description", "overall_soundscape", "non_diegetic_music"]
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
FIELD_RE = re.compile(r"^\s*(" + "|".join(FIELDS) + r")\s*:", re.M)
SHOT_RE = re.compile(r"\[Shot\s+(\d+)\]")
VOICE_RE = re.compile(r"\((S\d+)\)")
TRANS_RE = re.compile(r"</?scenetrans\s*>")
CHAR_RE = re.compile(r"[A-Za-z0-9\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
                     r"\U00020000-\U0002fa1f]")
RANGES = {"ordinary": (45, 70), "urgent": (55, 80), "action": (20, 55)}
MANUAL_CHECKS = [
    "逐镜按实际可用说话时间复核语速、停顿与对白可演性。",
    "人工复核参考图类型、身份及重要性排序；文本映射不能证明图片内容正确。",
    "人工复核切镜是否真实有效、空间与人物连续性，以及动作覆盖是否足够。",
    "人工复核段落类别及state_changes是否为不同且实际可见的状态变化；脚本仅计数。",
    "人工复核同一(Sn)是否始终绑定同一人物、声线与声音来源。",
    "本报告不验证成片、实际发声、口型或最终生成效果。",
]


def tag(name):
    return f"{{{NS}}}{name}"


def text_content(element):
    return "".join(node.text or "" for node in element.iter(tag("t")))


def column_index(address):
    match = re.match(r"([A-Z]+)", address)
    if not match:
        raise ValueError(f"无效单元格地址：{address}")
    value = 0
    for char in match.group(1):
        value = value * 26 + ord(char) - ord("A") + 1
    return value - 1


def read_xlsx(path):
    """Return populated rows in workbook order, resolving shared/inline strings."""
    sheets = []
    with zipfile.ZipFile(path) as archive:
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            shared = [text_content(item) for item in
                      ET.fromstring(archive.read("xl/sharedStrings.xml"))]
        relationships = {
            node.attrib["Id"]: node.attrib["Target"]
            for node in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
            if node.get("TargetMode") != "External"
        }
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        for sheet in workbook.findall(f"{tag('sheets')}/{tag('sheet')}"):
            target = relationships[sheet.attrib[f"{{{REL_NS}}}id"]]
            member = (target.lstrip("/") if target.startswith("/") else
                      posixpath.normpath(posixpath.join("xl", target)))
            root = ET.fromstring(archive.read(member))
            rows = []
            for fallback_row, row in enumerate(root.findall(
                    f"{tag('sheetData')}/{tag('row')}"), 1):
                values = {}
                for fallback_col, cell in enumerate(row.findall(tag("c"))):
                    index = (column_index(cell.attrib["r"]) if "r" in cell.attrib
                             else fallback_col)
                    kind = cell.get("t")
                    value_node = cell.find(tag("v"))
                    value = value_node.text or "" if value_node is not None else ""
                    if kind == "s":
                        value = shared[int(value)]
                    elif kind == "inlineStr":
                        value = text_content(cell)
                    if value != "":
                        values[index] = value
                if values:
                    width = max(values) + 1
                    rows.append((int(row.get("r", fallback_row)),
                                 [values.get(i, "") for i in range(width)]))
            sheets.append((sheet.get("name", member), rows))
    return sheets


def sequence_number(value):
    # Excel can serialize an integer-valued numeric cell as 1.0.
    raw = str(value).strip()
    if not re.fullmatch(r"[0-9]+(?:\.0+)?", raw):
        return None
    number = int(raw.split(".")[0])
    return number if number > 0 else None


def clean_dialogue(text):
    # Only strip tag-boundary whitespace and the explicit scene-transition tag.
    # Punctuation and all internal whitespace remain significant.
    return TRANS_RE.sub("", text).strip()


def read_json(path, label, errors):
    try:
        with open(path, encoding="utf-8-sig") as stream:
            data = json.load(stream)
        if not isinstance(data, list):
            raise ValueError("顶层必须为数组")
        return data
    except (OSError, ValueError) as exc:
        errors.append(f"{label}无法读取：{exc}")
        return None


def load_plan(path, errors):
    data = read_json(path, "plan-json", errors)
    if data is None:
        return {}
    plan = {}
    for index, item in enumerate(data, 1):
        if not isinstance(item, dict):
            errors.append(f"plan-json第{index}项必须为对象")
            continue
        seq = sequence_number(item.get("seq", ""))
        if seq is None or seq in plan:
            errors.append(f"plan-json第{index}项seq无效或重复")
            continue
        if item.get("mode") not in RANGES:
            errors.append(f"plan-json序号{seq}的mode必须为ordinary、urgent或action")
        changes = item.get("state_changes", [])
        if not isinstance(changes, list) or any(
                not isinstance(change, str) or not change.strip() for change in changes):
            errors.append(f"plan-json序号{seq}的state_changes必须为非空文本数组")
            changes = []
        if item.get("mode") == "action" and len(changes) < 3:
            errors.append(f"plan-json序号{seq}的action至少需要3个state_changes")
        plan[seq] = item
    return plan


def check_prompt(prompt, refs, context, errors):
    def fail(message):
        errors.append(f"{context}：{message}")

    if not prompt.lstrip().startswith("subject_definitions:"):
        fail("提示词必须从subject_definitions:开始，不加标题或导演分析前缀")
    field_matches = list(FIELD_RE.finditer(prompt))
    if [match.group(1) for match in field_matches] != FIELDS:
        fail("六字段必须各出现一次，且顺序为" + "、".join(FIELDS))
    fields = {}
    for index, match in enumerate(field_matches):
        end = field_matches[index + 1].start() if index + 1 < len(field_matches) else len(prompt)
        fields[match.group(1)] = prompt[match.end():end].strip()
        if not fields[match.group(1)]:
            fail(f"字段{match.group(1)}内容为空")

    definitions = fields.get("subject_definitions", "")
    subjects = list(re.finditer(r"<Subject\s+(\d+)>", definitions))
    defined = set()
    for index, match in enumerate(subjects):
        number = int(match.group(1))
        if number in defined:
            fail(f"<Subject {number}>重复定义")
        defined.add(number)
        end = subjects[index + 1].start() if index + 1 < len(subjects) else len(definitions)
        body = definitions[match.end():end]
        pictures = [int(value) for value in re.findall(r"\bfrom\s+<Picture\s+(\d+)>", body)]
        if pictures != [number]:
            fail(f"<Subject {number}>必须对应且仅对应from <Picture {number}>")
        if number < 1 or number > 5 or not refs[number - 1]:
            fail(f"<Subject {number}>没有对应的非空参考图槽位")
    for number, path in enumerate(refs, 1):
        if path and number not in defined:
            fail(f"参考图{number}缺少<Subject {number}> ... from <Picture {number}>定义")

    detailed = fields.get("detailed_description", "")
    shots = list(SHOT_RE.finditer(detailed))
    shot_ids = [int(match.group(1)) for match in shots]
    if len(shots) not in (3, 4):
        fail(f"每组必须有3或4个[Shot N]，实际{len(shots)}个")
    if shot_ids != list(range(1, len(shots) + 1)):
        fail(f"Shot编号必须从1连续递增，实际{shot_ids}")
    starts = []
    previous_start = 0.0
    for index, match in enumerate(shots):
        end = shots[index + 1].start() if index + 1 < len(shots) else len(detailed)
        body = detailed[match.end():end]
        if index == 0:
            starts.append(0.0)
            if re.search(r"\bAt\s+\d{2}:\d{2}(?:\.\d+)?", body):
                fail("Shot 1不能带At时间")
        else:
            timestamp = re.match(r"\s*At\s+00:(\d{2})\.(\d{3})(?=[,，\s]|$)", body)
            if timestamp is None:
                fail(f"Shot {shot_ids[index]}必须以At 00:SS.mmm时间开始")
            else:
                seconds = int(timestamp.group(1)) + int(timestamp.group(2)) / 1000
                starts.append(seconds)
                if not previous_start < seconds < 15:
                    fail(f"Shot {shot_ids[index]}时间必须严格递增且0<t<15，实际{seconds:g}")
                previous_start = seconds
        for number in map(int, re.findall(r"<Subject\s+(\d+)>", body)):
            if number not in defined:
                fail(f"Shot {shot_ids[index]}引用了未定义的<Subject {number}>")

    dialogue_matches = list(re.finditer(r"<d>(.*?)</d>", detailed, re.S))
    if detailed.count("<d>") != len(dialogue_matches) or detailed.count("</d>") != len(dialogue_matches):
        fail("对白<d>与</d>标签不成对")
    dialogues = []
    previous_end = 0
    speaker = None
    for index, match in enumerate(dialogue_matches, 1):
        prefix = detailed[previous_end:match.start()]
        voices = VOICE_RE.findall(prefix)
        if voices:
            speaker = voices[-1]
        elif TRANS_RE.sub("", prefix).strip() or speaker is None:
            speaker = None
            fail(f"第{index}段对白前缺少(Sn)声线标签，例如(S1)")
        content = re.match(r"\s*\[Chinese\](.*)\Z", match.group(1), re.S)
        if content is None:
            fail(f"第{index}段对白缺少[Chinese]语言标签")
            text = clean_dialogue(match.group(1))
        else:
            text = clean_dialogue(content.group(1))
        dialogues.append({"speaker_id": speaker, "text": text})
        previous_end = match.end()
    character_count = sum(len(CHAR_RE.findall(item["text"])) for item in dialogues)
    if character_count > 80:
        fail(f"本组对白{character_count}字，超过80字上限（计汉字及英数字字符）")
    return dialogues, {"shot_count": len(shots), "shot_starts_seconds": starts,
                       "dialogue_segments": len(dialogues), "dialogue_characters": character_count}


def merge_dialogue(items):
    merged = []
    for item in items:
        if merged and merged[-1]["speaker_id"] == item["speaker_id"]:
            merged[-1]["text"] += item["text"]
        else:
            merged.append(dict(item))
    return merged


def mismatch(expected, actual):
    index = next((i for i, pair in enumerate(zip(expected, actual)) if pair[0] != pair[1]),
                 min(len(expected), len(actual)))
    return (f"第{index + 1}个字符起不同；原文长度{len(expected)}，实际长度{len(actual)}；"
            f"原文片段{expected[max(0, index - 8):index + 16]!r}，"
            f"实际片段{actual[max(0, index - 8):index + 16]!r}")


def check_original(path, actual, errors, warnings):
    expected = read_json(path, "dialogue-json", errors)
    if expected is None:
        return
    if all(isinstance(item, str) for item in expected):
        wanted = "".join(clean_dialogue(item) for item in expected)
        found = "".join(item["text"] for item in actual)
        if wanted != found:
            errors.append("全片对白逐字不匹配：" + mismatch(wanted, found))
        warnings.append("dialogue-json为字符串数组，仅核对全文，未核对说话者顺序")
        return
    if not all(isinstance(item, dict) and isinstance(item.get("text"), str)
               and isinstance(item.get("speaker_id"), str)
               and re.fullmatch(r"S\d+", item["speaker_id"]) for item in expected):
        errors.append("dialogue-json必须为字符串数组，或含speaker_id='Sn'与text的对象数组")
        return
    wanted = merge_dialogue([{"speaker_id": item["speaker_id"],
                              "text": clean_dialogue(item["text"])} for item in expected])
    found = merge_dialogue(actual)
    if len(wanted) != len(found):
        errors.append(f"合并相邻同speaker片段后对白段数不匹配：原文{len(wanted)}，实际{len(found)}")
    for index, (left, right) in enumerate(zip(wanted, found), 1):
        if left["speaker_id"] != right["speaker_id"]:
            errors.append(f"对白第{index}段说话者不匹配：原文{left['speaker_id']}，实际{right['speaker_id']}")
        if left["text"] != right["text"]:
            errors.append(f"对白第{index}段逐字不匹配：" + mismatch(left["text"], right["text"]))


def validate(args):
    report = {"errors": [], "warnings": [], "stats": {"groups": []},
              "manual_checks": MANUAL_CHECKS}
    errors, warnings, stats = report["errors"], report["warnings"], report["stats"]
    plan = load_plan(args.plan_json, errors) if args.plan_json else None
    if plan is None:
        warnings.append("未提供plan-json：未按ordinary/urgent/action段落类别核验字数与状态变化数量")
    if not args.dialogue_json:
        warnings.append("未提供dialogue-json：未与原剧本逐字核验对白及说话者顺序")
    try:
        sheets = read_xlsx(args.xlsx)
    except (OSError, ValueError, KeyError, IndexError, ET.ParseError, zipfile.BadZipFile) as exc:
        errors.append(f"无法读取xlsx：{exc}")
        return report
    if [name for name, _ in sheets[:2]] != ["任务表", "填写说明"]:
        errors.append("工作表名称与顺序必须为：第一张“任务表”，第二张“填写说明”")
    # The contract fixes the first sheet; do not search for a convenient match.
    candidates = sheets[:1]
    if not candidates or not candidates[0][1]:
        errors.append("xlsx第一张工作表没有非空任务表数据")
        return report
    stats["task_sheets"] = [name for name, _ in candidates]
    stats["ignored_sheets"] = [name for name, _ in sheets if name not in stats["task_sheets"]]
    all_dialogues, all_sequences = [], []
    for name, rows in candidates:
        header_row, headers = rows[0]
        if headers != HEADERS:
            errors.append(f"{name}第{header_row}行表头必须严格为九列：" + "、".join(HEADERS))
        if len(rows) == 1:
            errors.append(f"{name}没有分镜数据行")
        sheet_sequences = []
        for row_number, values in rows[1:]:
            context = f"{name}第{row_number}行"
            if len(values) > 9:
                errors.append(f"{context}：九列之外存在非空数据")
            cells = (values + [""] * 9)[:9]
            seq = sequence_number(cells[1])
            if seq is None:
                errors.append(f"{context}：分镜序号必须为正整数，可用01、001或数值")
            else:
                sheet_sequences.append(seq)
                all_sequences.append(seq)
            if cells[7] not in ("是", "否"):
                errors.append(f"{context}：H列只能是“是”或“否”，不得附解释")
            refs = cells[2:7]
            empty_seen = False
            for number, path in enumerate(refs, 1):
                if not path:
                    empty_seen = True
                else:
                    if empty_seen:
                        errors.append(f"{context}：参考图{number}之前有空槽")
                    if not re.fullmatch(r"assets\\[^\\/\r\n]+\.png", path):
                        errors.append(f"{context}：参考图{number}路径必须为assets\\名称.png")
            dialogues, group = check_prompt(cells[8], refs, context, errors)
            all_dialogues.extend(dialogues)
            group.update({"sheet": name, "row": row_number, "seq": seq,
                          "reference_count": sum(bool(path) for path in refs)})
            if plan is not None:
                item = plan.get(seq)
                if item is None:
                    errors.append(f"{context}：plan-json中缺少序号{seq}")
                elif item.get("mode") in RANGES:
                    mode = item["mode"]
                    low, high = RANGES[mode]
                    group["mode"] = mode
                    if not low <= group["dialogue_characters"] <= high:
                        errors.append(f"{context}：{mode}须为{low}—{high}字，实际{group['dialogue_characters']}字")
            stats["groups"].append(group)
        duplicates = [seq for seq, count in Counter(sheet_sequences).items() if count > 1]
        if duplicates:
            errors.append(f"{name}：分镜序号重复{duplicates}")
        if sheet_sequences != list(range(1, len(rows))):
            errors.append(f"{name}：分镜序号必须按实际行顺序从1连续递增到{len(rows) - 1}")
    if plan is not None:
        extra = sorted(set(plan) - set(all_sequences))
        if extra:
            errors.append(f"plan-json存在任务表中没有的序号{extra}")
    if args.dialogue_json:
        check_original(args.dialogue_json, all_dialogues, errors, warnings)
    stats["group_count"] = len(stats["groups"])
    stats["shot_count"] = sum(group["shot_count"] for group in stats["groups"])
    stats["dialogue_characters"] = sum(group["dialogue_characters"] for group in stats["groups"])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xlsx", type=Path, required=True)
    parser.add_argument("--dialogue-json", type=Path)
    parser.add_argument("--plan-json", type=Path)
    report = validate(parser.parse_args())
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
