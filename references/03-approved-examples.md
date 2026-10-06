# 完整行样例：精简执行版

前三个样例依据《丈母娘拦女婿送冻饺子》的既有用户认可成品精简，**不是原交付的逐字复刻**。原对白、说话人、关键动作、镜头数量和时间点保留；以下精简执行版作为默认模仿样例。正文主要写景别、必要站位、谁对谁说、简单表情语气，以及不可省略的动作、声源和实际运镜，不复述内部导演分析。

拿走饺子、银行卡放桌与拒收、绕过茶几坐到母亲身旁等动作完整保留，不为省词删掉动作结果；也不因对白出现身体部位或物件名称就加触摸、指认或拿放。末例是教学样例，非用户验收成品。不迁移样例人物、台词、商品、组数或总长；新剧本逐镜重算时间。每例均为15秒，不设描述字数上限。

## 目录

- [用户认可样例：原第1组](#样例原第1组)
- [用户认可样例：原第11组](#样例原第11组)
- [用户认可样例：原第13组](#样例原第13组)
- [新增教学样例：信息揭示驱动镜头](#新增教学样例信息揭示驱动镜头)

## 样例：原第1组

争执：一句命令同时截停演员与摄影机；拿走饺子改变人物行动。

参考图依次：
- `assets\丈母娘_粉衣绿马甲.png`
- `assets\明远_棕色夹克.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：否。

完整提示词（精简执行版）：

```text
subject_definitions:
<Subject 1> is Zhixia's mother, Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Mingyuan, about thirty, with short black hair, a brown jacket, dark brown collared shirt, dark gray trousers and a black left-wrist watch, from <Picture 2>.
<Subject 3> is the modern home: pale sofa, wooden coffee table and TV console, dark entry door; use layout and daylight only, excluding pictured people, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family drama. Mother stops Mingyuan leaving for the hospital and takes his dumplings.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - home layout, furniture and daylight.
detailed_description: Photorealistic, soft daylight and warm room light. Current state: In <Subject 3>, <Subject 2> heads toward the entry with two clear bags of frozen dumplings in his right hand; <Subject 1> catches up.
[Shot 1] Knee-up two-shot: <Subject 2> moves screen right; <Subject 1> approaches from screen left. Track his last half-step, then stop with him on her command. <Subject 1> (S1), in a slightly husky older female Mandarin voice, shouts to him <d>[Chinese] 站住！</d>.
[Shot 2] At 00:01.000, Cut to a waist-up two-shot on the same axis, showing the two bags of pale, flour-dusted raw dumplings. Push slightly toward <Subject 1>'s stern face, keeping <Subject 2>'s tense profile at frame right. <Subject 1> (S1) forcefully asks him <d>[Chinese] 你妈摔断了腿，你就拎着两袋冻了半个月的饺子去医院？</d>.
[Shot 3] At 00:05.800, Cut to a fixed medium close-up of <Subject 2>, with <Subject 1>'s right shoulder at the edge. <Subject 2> (S2), in a warm mid-register young adult male Mandarin voice, anxiously explains to her <d>[Chinese] 妈，您都知道了？我爸刚打电话，说我妈在医院等手术。我想着她爱吃饺子，等出院了给她煮。</d>.
[Shot 4] At 00:12.300, Cut to a fixed waist-up two-shot showing faces and bag handles, the closed door behind <Subject 2>. <Subject 1> takes both bag handles from <Subject 2>'s right hand; he releases them and ends empty-handed. <Subject 1> (S1) firmly tells him <d>[Chinese] 这饺子是我留着吃的，你放下。</d>.
overall_soundscape: Quiet home ambience; stable speaker voices, listeners' lips closed.
non_diegetic_music: Restrained low strings below dialogue.
```

## 样例：原第11组

道具：银行卡落桌声触发短物件镜头，母亲台词跨切不断，女儿拒绝动作承接。

参考图依次：
- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：是。

完整提示词（精简执行版）：

```text
subject_definitions:
<Subject 1> is Zhixia's mother, Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a short beige trench-style jacket, gray collared top and light trousers; her brown shoulder bag is removable, from <Picture 2>.
<Subject 3> is the modern home: pale sofa, wooden coffee table and TV console, dark entry door; use layout and daylight only, excluding pictured people, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family drama. Mother offers her retirement savings; Zhixia refuses the bank card.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - identity, hair and clothing.
<Subject 2> (appears in [Shot 3], [Shot 4]): fully_preserved - identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - home layout, furniture and daylight.
detailed_description: Photorealistic, soft daylight and warm room light. Current state: In <Subject 3>, <Subject 1> sits forward, right hand approaching her vest pocket; <Subject 2> stands opposite across the clear coffee table.
[Shot 1] Continue a clean medium close-up of <Subject 1>. She takes one navy bank card from her vest pocket with her right hand and places it on the table; tilt down slightly with the placement. <Subject 1> (S1), in a slightly husky older female Mandarin voice, steadily tells <Subject 2> <d>[Chinese] 这里有五万块，是我攒的养老钱。<scenetrans></d>. The card taps the table.
[Shot 2] At 00:03.600, Cut on the tap to an overhead detail: one navy card lies flat on the table; <Subject 1>'s fingertips withdraw. <Subject 1> (S1), off-screen at the same seat, continues gently to <Subject 2> without a restart <d>[Chinese] <scenetrans>密码是你生日。<scenetrans></d>.
[Shot 3] At 00:04.900, Cut to a fixed waist-up two-shot with the card between them. <Subject 2> reaches toward it, then stops before touching it. <Subject 1> (S1) continues firmly to her <d>[Chinese] <scenetrans>拿去给你婆婆做手术，该检查就检查，该用药就用药。</d>.
[Shot 4] At 00:10.900, Cut to a medium close-up of <Subject 2>, including her hand and the untouched card low in frame, with <Subject 1>'s shoulder at frame right. <Subject 2> draws her hand back, tearful. <Subject 2> (S3), in a clear, slightly bright young adult female Mandarin voice, urgently tells her <d>[Chinese] 不行，这是您的养老钱，我不能拿。</d>.
overall_soundscape: Quiet home ambience and the card tap; Mother's speech continues across Shots 1–3. Stable speaker voices, listeners' lips closed.
non_diegetic_music: Warm, restrained piano below dialogue.
```

## 样例：原第13组

温情：女儿从对面绕到母亲身旁，横移以二人处于同侧为终点，关系变化可见。

参考图依次：
- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：否。

完整提示词（精简执行版）：

```text
subject_definitions:
<Subject 1> is Zhixia's mother, Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink top, dark green vest and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a short beige trench-style jacket, gray collared top and light trousers; her brown shoulder bag is removable, from <Picture 2>.
<Subject 3> is the modern home: pale sofa, wooden coffee table and TV console, dark entry door; use layout and daylight only, excluding pictured people, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family drama. Zhixia admits her mistake and sits beside Mother.
retention_analysis:
<Subject 1> (appears in [Shot 2], [Shot 3]): fully_preserved - identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - home layout, furniture and daylight.
detailed_description: Photorealistic, soft daylight and warm room light. Current state: In <Subject 3>, <Subject 2> stands left of the table wearing her brown shoulder bag; <Subject 1> sits on the sofa right. The card remains on the table.
[Shot 1] Fixed, clean medium close-up of <Subject 2>. <Subject 2> (S3), tearful and remorseful, in a clear, slightly bright young adult female Mandarin voice, tells her mother <d>[Chinese] 妈，是我钻牛角尖了。<scenetrans></d>.
[Shot 2] At 00:04.000, Cut to a medium-wide two-shot. <Subject 2> removes her bag, places it on the sofa arm, walks around the table's open end and sits beside <Subject 1>. Move laterally with her, ending with both women on the same side and the card in front. <Subject 2> (S3) continues remorsefully to her mother without a restart <d>[Chinese] <scenetrans>我只记着自己受的委屈，却忘了明远这些年受的累。</d>.
[Shot 3] At 00:09.100, Cut to a tighter, eye-level seated two-shot. <Subject 1> turns toward <Subject 2>. <Subject 1> (S1), in a slightly husky older female Mandarin voice, gently tells her <d>[Chinese] 一家人过日子，不怕吃点亏，就怕人人都只算自己的账。</d>.
overall_soundscape: Quiet home ambience; Zhixia's speech continues across Shots 1–2. Stable speaker voices, listeners' lips closed.
non_diegetic_music: Warm, restrained piano below dialogue.
```

## 新增教学样例：信息揭示驱动镜头

**教学样例的精简执行版，非既有用户验收成片。** 用于演示先确定信息归属，再写必要构图和表情语气；不把减少肢体动作当成新的全片风格。

教学原稿事实：林清向赵姨询问失散哥哥的辨认依据。哥哥不在现场，右手腕旧疤属于哥哥；救妹妹的往事及父亲日记是本段原稿明确给出的信息。日记尚未拿到现场。本段原稿没有触摸手腕、出示日记或起身离开的动作。林清想知道为何被隐瞒，赵姨先解释隐瞒原因，再提供可核实的记录出处。

原对白依次为：

- 赵姨：“你哥哥右手腕有一道旧疤，是小时候救你留下的。”
- 林清：“您以前怎么从来没跟我说过？”
- 赵姨：“我怕你自责。你父亲当年的日记里，把那天的事记得清清楚楚。”

规划：ordinary，57个对白汉字；三镜分别为0—4.8秒、4.8—8.2秒、8.2—15秒。信息变化为“辨认特征连到林清本人 → 林清质问隐瞒 → 赵姨解释并给出记录出处”。按对白和换气规划时间，尚未实测配音。三镜都有正在发生的交流，不靠沉默延长。

参考图依次（教学示意，未随 Skill 提供这些 PNG）：

- `assets\林清_米色针织衫.png`
- `assets\赵姨_深蓝衬衫.png`
- `assets\旧居客厅.png`

林清是本故事主角，图槽优先于赵姨；全片声线分别为 S2、S5，与本组 Subject 1、Subject 2 独立。继承上一镜尾帧：否。

完整提示词（精简执行版）：

```text
subject_definitions:
<Subject 1> is Lin Qing, a young adult Chinese woman with shoulder-length black hair and a cream knit sweater, from <Picture 1>.
<Subject 2> is Aunt Zhao, an older Chinese woman with short gray-black hair and a dark-blue blouse, from <Picture 2>.
<Subject 3> is the modest living room with two chairs beside a window and soft afternoon daylight; use layout and light only, excluding pictured people, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action Chinese family drama. Aunt Zhao reveals the brother's sacrifice and names a diary that records it.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - identity, hair and clothing.
<Subject 2> (appears in [Shot 1], [Shot 3]): fully_preserved - identity, hair and clothing.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - chair positions, window direction and afternoon daylight.
detailed_description: Photorealistic, consistent eyelines. Current state: In <Subject 3>, <Subject 1> sits frame left facing <Subject 2> on the right, discussing her absent brother.
[Shot 1] Fixed seated waist-up two-shot. <Subject 2> (S5), in a low, slightly husky older female Mandarin voice, solemnly tells <Subject 1> <d>[Chinese] 你哥哥右手腕有一道旧疤，是小时候救你留下的。</d>. <Subject 1> looks startled.
[Shot 2] At 00:04.800, Cut to a fixed, clean medium close-up of <Subject 1>, looking frame right toward <Subject 2>. <Subject 1> (S2), hurt and angry, in a clear young adult female Mandarin voice, asks <d>[Chinese] 您以前怎么从来没跟我说过？</d>.
[Shot 3] At 00:08.200, Cut to a clean medium close-up of <Subject 2>, looking frame left toward <Subject 1>. Push slowly to a close-up during her reply, stopping by its end. <Subject 2> (S5), in the same voice, answers quietly, then firmly <d>[Chinese] 我怕你自责。你父亲当年的日记里，把那天的事记得清清楚楚。</d>.
overall_soundscape: Quiet living-room ambience; stable speaker voices, listeners' lips closed.
non_diegetic_music: Faint piano under the disclosure, fading during Lin Qing's question.
```

本例的镜头任务由“消息如何改变眼前两人的交流”决定，而不是给旧疤安排触摸动作、给日记安排临时翻找。需要强动作的原稿仍应完整保留强动作；本例不能反向用作删掉争抢、拦阻、拥抱或证据交接的理由。
