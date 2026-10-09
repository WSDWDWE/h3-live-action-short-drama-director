# 完整行样例：精简修订示范

前三个样例基于用户认可的《丈母娘拦女婿送冻饺子》成品，保留原对白、标点、说话人和关键行动，按当前规则精简英文描述，并修正时间分配、景别与出镜记录。**本页是修订示范，不是用户已验收的新版成片。** 第四个为独立教学样例。

学习字段、参考绑定、具体表演、运镜及对白跨切写法；不迁移样例人物、台词、商品、组数或总时长。每例规划15秒，新剧本须重新分组计时。以下只完成文本规划，未实测配音或视频。

## 目录

- [修订样例：原第1组](#样例原第1组)
- [修订样例：原第11组](#样例原第11组)
- [修订样例：原第13组](#样例原第13组)
- [教学样例：信息揭示驱动镜头](#教学样例信息揭示驱动镜头)

## 样例：原第1组

争执：命令截停离开，追问接解释，拿走饺子阻止离开。urgent，共73个对白汉字。

修订：切点由1.000／5.800／12.300秒改为0.650／5.050／12.250秒，四镜时长为0.65／4.40／7.20／2.75秒；第三镜36个汉字，按急切语气预留7.20秒。末镜改为能同时容纳脸、手和袋子的中景。移除配乐及所有音效描述。

参考图依次：

- `assets\丈母娘_粉衣绿马甲.png`
- `assets\明远_棕色夹克.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：否。

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, a dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Mingyuan, about thirty, with short black hair, a brown jacket, a dark brown shirt, dark gray trousers and a black watch on his left wrist, from <Picture 2>.
<Subject 3> is the modern living room and entryway with a pale sofa, wooden coffee table and dark entry door; use its layout and light, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family-drama sequence. Mother stops Mingyuan at the door and takes his two bags of frozen dumplings.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain layout and light.
detailed_description: No subtitles or captions. Photorealistic contemporary Chinese family drama. Only the named speaker moves lips. Current state: In <Subject 3>, Mingyuan approaches the door with two clear bags of frozen uncooked dumplings in his right hand; Mother follows from the living room.
[Shot 1] From 00:00.000 to 00:00.650, use a knee-up lateral two-shot. <Subject 2> moves screen right; <Subject 1> approaches from screen left. Track his last half-step, then stop with him at her command. <Subject 1> (S1), in a slightly husky older female Mandarin voice, says <d>[Chinese] 站住！</d>. Delivery: loud and sharply commanding.
[Shot 2] At 00:00.650, Cut on his stop to a waist-up two-shot from the same side. <Subject 1> indicates the two bags and fixes <Subject 2> with an angry stare. Push closer to her face, retaining his tense profile at frame right. <Subject 1> (S1), says <d>[Chinese] 你妈摔断了腿，你就拎着两袋冻了半个月的饺子去医院？</d>. Delivery: fast, incredulous and forceful.
[Shot 3] At 00:05.050, Cut to <Subject 2> in medium close-up, with <Subject 1>'s right shoulder at frame left. He addresses her anxiously, then glances at the door while holding the bags down. Keep the camera steady. <Subject 2> (S2), in a warm, mid-register young adult male Mandarin voice, says <d>[Chinese] 妈，您都知道了？我爸刚打电话，说我妈在医院等手术。我想着她爱吃饺子，等出院了给她煮。</d>. Delivery: quick, anxious and pleading.
[Shot 4] At 00:12.250, Cut as <Subject 1> reaches for the handles to a medium two-shot including both faces, hands and bags. She firmly takes both bags from <Subject 2>; he releases them and draws his empty hand back. The closed door remains behind him. <Subject 1> (S1), says <d>[Chinese] 这饺子是我留着吃的，你放下。</d>. Delivery: firm and final. End at 00:15.000 with Mother holding both bags and Mingyuan facing her empty-handed.
overall_soundscape: Dialogue only. No ambient sound or sound effects.
non_diegetic_music: None.
```

## 样例：原第11组

道具：银行卡放下触发物件镜头，母亲的原句跨切不断，女儿伸手后收回。ordinary，共53个对白汉字。

修订：保留3.600／4.900／10.900秒切点；第一镜只拍母亲，出镜记录据此修正。末镜使用容纳女儿脸、手与桌面银行卡的侧面中景。切点由可见动作触发，不依赖落桌声。

参考图依次：

- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：是。

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, a dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a beige jacket, a gray collared top and light trousers, from <Picture 2>.
<Subject 3> is the modern living room and entryway with a pale sofa, wooden coffee table and dark entry door; use its layout and light, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family-drama sequence. Mother places a bank card on the table; Zhixia refuses to take it.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing.
<Subject 2> (appears in [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain layout and light.
detailed_description: No subtitles or captions. Photorealistic contemporary Chinese family drama. Only the named speaker moves lips. Current state: In <Subject 3>, Mother sits forward on the sofa, reaching into her vest pocket with her right hand. Zhixia stands across the coffee table with her brown shoulder bag on.
[Shot 1] From 00:00.000 to 00:03.600, continue a medium close-up of <Subject 1> addressing Zhixia. She takes one navy bank card from her vest pocket and places it on the table; tilt down with her hand to the placement. <Subject 1> (S1), in a slightly husky older female Mandarin voice, says <d>[Chinese] 这里有五万块，是我攒的养老钱。<scenetrans></d>. Delivery: steady and matter-of-fact.
[Shot 2] At 00:03.600, Cut on the card reaching the table to an overhead detail of the navy card lying flat. <Subject 1>'s right fingertips withdraw. <Subject 1> (S1), off-screen beside the table, continues seamlessly with <d>[Chinese] <scenetrans>密码是你生日。<scenetrans></d>. Delivery: the same voice, softening gently.
[Shot 3] At 00:04.900, Cut back to a medium two-shot across the table, <Subject 1> seated frame left and <Subject 2> standing frame right. The card lies between them. Mother draws her right hand back; Zhixia leans toward the table and reaches for the card, stopping short of touching it. <Subject 1> (S1), continues seamlessly with <d>[Chinese] <scenetrans>拿去给你婆婆做手术，该检查就检查，该用药就用药。</d>. Delivery: practical and unwavering.
[Shot 4] At 00:10.900, Cut on the stopped hand to a closer side medium shot including <Subject 2>'s face, hand and the card; <Subject 1> remains at frame left. Zhixia immediately refuses and draws her hand back, looking at Mother with tearful eyes. <Subject 2> (S3), in a clear, slightly bright young adult female Mandarin voice, says <d>[Chinese] 不行，这是您的养老钱，我不能拿。</d>. Delivery: startled, urgent and worried. End at 00:15.000 with the card still on the table.
overall_soundscape: Dialogue only. No ambient sound or sound effects.
non_diegetic_music: None.
```

## 样例：原第13组

温情：女儿从对面坐到母亲身旁，横移跟随走位，再切近双人镜接母亲答话。ordinary，共51个对白汉字。

修订：切点由4.000／9.100秒改为2.500／8.800秒，首镜8个汉字不再占用4秒，中间镜头留6.30秒完成放包、绕桌和坐下。第三镜由原来的Hold改为真实切入更近的双人镜。首镜只拍女儿，母亲出镜记录据此修正。明确女儿坐到母亲自身右侧的空位，下一镜沿用落座后的邻座关系。

参考图依次：

- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：否。

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, a dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a beige jacket, a gray collared top and light trousers, from <Picture 2>.
<Subject 3> is the modern living room and entryway with a pale sofa, wooden coffee table and dark entry door; use its layout and light, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family-drama sequence. Zhixia apologizes and sits beside Mother.
retention_analysis:
<Subject 1> (appears in [Shot 2], [Shot 3]): fully_preserved - retain identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain layout and light.
detailed_description: No subtitles or captions. Photorealistic contemporary Chinese family drama. Only the named speaker moves lips. Current state: In <Subject 3>, Zhixia stands frame left beside the table, wearing her brown shoulder bag. Mother sits across the table on the sofa at frame right, with an empty seat on her own right. The navy bank card remains on the table.
[Shot 1] From 00:00.000 to 00:02.500, use a steady medium close-up of <Subject 2>. She looks from the table to Mother off-screen right, lowers her chin and loosens her grip on the bag strap. <Subject 2> (S3), in a clear, slightly bright young adult female Mandarin voice, says <d>[Chinese] 妈，是我钻牛角尖了。<scenetrans></d>. Delivery: tearful and apologetic.
[Shot 2] At 00:02.500, Cut as <Subject 2> takes off her bag to a medium-wide two-shot. She sets the bag on the nearer sofa arm, walks around the open end of the table and sits in the empty seat on <Subject 1>'s right, continuing her sentence. Track laterally with her and stop with <Subject 2> seated frame left and <Subject 1> frame right, both facing the table with the card in front of them. <Subject 2> (S3), continues seamlessly with <d>[Chinese] <scenetrans>我只记着自己受的委屈，却忘了明远这些年受的累。</d>. Delivery: remorseful and clear throughout the move.
[Shot 3] At 00:08.800, Cut as <Subject 1> turns to her seated daughter to a closer eye-level two-shot from the same side, keeping <Subject 2> frame left and <Subject 1> frame right in the same seats. Mother speaks gently; <Subject 2> meets her eyes and straightens slightly. Keep the camera steady through the reply. <Subject 1> (S1), in a slightly husky older female Mandarin voice, says <d>[Chinese] 一家人过日子，不怕吃点亏，就怕人人都只算自己的账。</d>. Delivery: warm and plainspoken. End at 00:15.000 with both women seated together.
overall_soundscape: Dialogue only. No ambient sound or sound effects.
non_diegetic_music: None.
```

## 教学样例：信息揭示驱动镜头

本例为教学示范，非用户验收成片。原稿是一段坐着交谈的戏：赵姨说明辨认依据，林清追问，赵姨回答。本段没有展示证据或触碰身体的动作。对白中提到的信息不额外翻译成当前画面。

原对白依次为：

- 赵姨：“你哥哥右手腕有一道旧疤，是小时候救你留下的。”
- 林清：“您以前怎么从来没跟我说过？”
- 赵姨：“我怕你自责。你父亲当年的日记里，把那天的事记得清清楚楚。”

规划：ordinary，共57个对白汉字；三镜为0—4.8秒、4.8—8.2秒、8.2—15秒。保留原切点，三个镜头持续推进对白，未添加独立动作填时。

参考图依次（教学示意，未随 Skill 提供这些 PNG）：

- `assets\林清_米色针织衫.png`
- `assets\赵姨_深蓝衬衫.png`
- `assets\旧居客厅.png`

林清是故事主角，图槽优先于赵姨；全片声线分别为S2、S5，与本组Subject 1、Subject 2独立。继承上一镜尾帧：否。

完整提示词：

```text
subject_definitions:
<Subject 1> is Lin Qing, a young adult Chinese woman with shoulder-length black hair and a cream knit sweater, from <Picture 1>.
<Subject 2> is Aunt Zhao, an older Chinese woman with short gray-black hair and a dark-blue blouse, from <Picture 2>.
<Subject 3> is the modest living room with two chairs beside a window in afternoon daylight; use its layout and light, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family-drama sequence. Lin Qing questions Aunt Zhao during their seated conversation.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - retain identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 3]): fully_preserved - retain identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain chair positions, window direction and daylight.
detailed_description: No subtitles or captions. Photorealistic contemporary Chinese family drama. Only the named speaker moves lips. Current state: In <Subject 3>, <Subject 1> sits frame left facing <Subject 2> seated on the right.
[Shot 1] From 00:00.000 to 00:04.800, use a steady waist-up two-shot. <Subject 2> speaks directly to <Subject 1>, whose expression grows tense as she listens. <Subject 2> (S5), in a low, slightly husky older female Mandarin voice, says <d>[Chinese] 你哥哥右手腕有一道旧疤，是小时候救你留下的。</d>. Delivery: measured and serious.
[Shot 2] At 00:04.800, Cut at the end of Zhao's sentence to a clean medium close-up of <Subject 1> looking frame right at Zhao. She questions her immediately with a hurt, angry expression. <Subject 1> (S2), in a clear young adult female Mandarin voice, says <d>[Chinese] 您以前怎么从来没跟我说过？</d>. Delivery: urgent, rising in pitch on the question.
[Shot 3] At 00:08.200, Cut as Zhao answers to a clean medium close-up of <Subject 2> looking frame left at Lin Qing. Make one slow push toward her face, ending in a close-up. <Subject 2> (S5), in the same older female Mandarin voice, says <d>[Chinese] 我怕你自责。你父亲当年的日记里，把那天的事记得清清楚楚。</d>. Delivery: subdued at first, then firm and clear. Complete the reply and push by 00:15.000.
overall_soundscape: Dialogue only. No ambient sound or sound effects.
non_diegetic_music: None.
```

本例用景别、眼神、表情、语气和一次推近完成这段交流；不据此删减其他原稿中的争抢、拦阻、拥抱、证据交接或商品操作。
