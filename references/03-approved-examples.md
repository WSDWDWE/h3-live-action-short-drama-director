# 用户认可的完整行样例

前三个样例来自《丈母娘拦女婿送冻饺子》的实际交付，正文保留。学习字段、绑定，以及“人物为什么行动 → 行动改变什么 → 镜头怎样呈现”的因果，不模仿动作数量或每镜的动作种类。拿走饺子阻止离开、放下银行卡提出实际帮助、从对面坐到身旁改变关系；这些依据成立，动作才成立。不能因为新台词出现身体部位或物件名称，就照着安排触摸、指认或拿放。

末尾新增一个信息揭示驱动的教学样例，与前三个用户认可成品明确区分。不迁移任何样例的人物、台词、商品、28组或7分钟总长。时间点只服务该段内容，新剧本逐镜重算。每个样例均为15秒。

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

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink long-sleeved top under a dark green vest, and dark trousers, from <Picture 1>.
<Subject 2> is Mingyuan, about thirty, with short black hair, a brown jacket over a dark brown collared shirt, dark gray trousers, and a black watch on his left wrist, from <Picture 2>.
<Subject 3> is the consistent modern home interior with a pale sofa, wooden coffee table and TV console, a dark entry door, and a clear route between living room and entry; use the room layout and daylight only, with people supplied separately, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action family-drama sequence. Mother stops an urgent hospital departure and takes the frozen dumplings, creating a painful misunderstanding.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain the home layout, furniture and daylight in the home shots.
detailed_description: Photorealistic contemporary Chinese family drama, natural skin texture and consistent soft daylight mixed with warm room light. Play the dialogue as continuous human exchanges with actions underneath, keeping speaker voices stable. Current state: Mingyuan is walking from the sofa toward the dark entry door with two clear bags of frozen dumplings in his right hand; Mother catches up from inside the room.
[Shot 1] In <Subject 3>, start a knee-up lateral two-shot with <Subject 2> moving screen right toward the door and <Subject 1> approaching from screen left. Track only his last half-step; her command arrests both him and the camera. Cut on his arrested foot. <Subject 1> (S1), in a slightly husky, direct older female Mandarin voice, says <d>[Chinese] 站住！</d>. Delivery: an abrupt, hard-edged command, already loud on the first word. Sound: A shoe scuffs to a halt; the bags jerk and crackle.
[Shot 2] At 00:01.000, Cut to a waist-up two-shot at the same side of the doorway axis. <Subject 1> indicates the pale, flour-dusted uncooked dumplings inside two separate clear bags, then fixes <Subject 2> with a hard stare. Push slightly from the bags-and-faces composition to her accusing face as she stresses their age; end with his tense profile still at frame right. <Subject 1> (S1), says <d>[Chinese] 你妈摔断了腿，你就拎着两袋冻了半个月的饺子去医院？</d>. Delivery: clipped, incredulous and forceful, stressing the frozen leftovers rather than insulting his mother. Sound: Thin plastic rustle stays under the accusation; a low pulse begins beneath speech.
[Shot 3] At 00:05.800, Cut on the mention of hospital to <Subject 2> in medium close-up, with only <Subject 1>'s identified right shoulder at the frame edge. He explains in one urgent breath, first searching her face, then glancing toward the door while keeping the bags down. Hold steady so the wish to leave is legible; cut when her hand enters toward the bag handles. <Subject 2> (S2), in a warm, mid-register young adult male Mandarin voice, says <d>[Chinese] 妈，您都知道了？我爸刚打电话，说我妈在医院等手术。我想着她爱吃饺子，等出院了给她煮。</d>. Delivery: quick, anxious and breath-connected; fear for his mother, with a slight pleading lift at the end. Sound: His rushed inhalation and the creak of the bag handles are audible; the elder remains silent.
[Shot 4] At 00:12.300, Cut to a waist-level two-shot that retains both faces. <Subject 1> takes both handles from <Subject 2> with a single firm transfer as she speaks; he releases them, recoils only at the wrist, and ends empty-handed facing her. Keep the camera fixed on the transfer, with the closed door behind him. <Subject 1> (S1), says <d>[Chinese] 这饺子是我留着吃的，你放下。</d>. Delivery: flat, possessive and final, with a hard emphasis on the command to put them down. Sound: Plastic changes hands with one crisp crackle; his half-started breath leads to the next group.
overall_soundscape: Quiet home room tone with only the specified footsteps, fabric and prop sounds; each line belongs to its named speaker and other visible characters listen with closed lips.
non_diegetic_music: Sparse low strings with a restrained tense pulse, below all speech.```

## 样例：原第11组

道具：银行卡落桌声触发短物件镜头，母亲台词跨切不断，女儿拒绝动作承接。

参考图依次：
- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：是。

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink long-sleeved top under a dark green vest, and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a beige short trench-style jacket over a gray collared top, and light trousers; her brown shoulder bag is a removable scene prop, from <Picture 2>.
<Subject 3> is the consistent modern home interior with a pale sofa, wooden coffee table and TV console, a dark entry door, and a clear route between living room and entry; use the room layout and daylight only, with people supplied separately, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action family-drama sequence. The navy bank card makes the retirement-savings sacrifice visible; the daughter refuses to take it.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 2> (appears in [Shot 1], [Shot 3], [Shot 4]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - retain the home layout, furniture and daylight in the home shots.
detailed_description: Photorealistic contemporary Chinese family drama, natural skin texture and consistent soft daylight mixed with warm room light. Play the dialogue as continuous human exchanges with actions underneath, keeping speaker voices stable. Current state: Continue Mother seated forward, her right hand moving toward her vest pocket. Zhixia stands opposite. The coffee table is clear nearest them.
[Shot 1] Continue <Subject 1>'s medium close-up as she brings one deep navy bank card out of her vest pocket and down toward the table. Her face remains the emotional subject; the camera tilts slightly with the completed placement so the decision has a visible consequence. <Subject 1> (S1), in a slightly husky, direct older female Mandarin voice, says <d>[Chinese] 这里有五万块，是我攒的养老钱。<scenetrans></d>. Delivery: clear and steady; stress fifty thousand yuan and retirement savings without announcing a spectacle. Sound: A single dry card tap marks the end of the placement.
[Shot 2] At 00:03.600, Cut on the tap to a brief overhead detail of the one card lying flat on the wooden coffee table, Mother's identified fingertips withdrawing. Its navy face has fine gold geometric lines and indistinct small lettering. The amount is spoken, not shown as a printed account balance. End once the card's position is unambiguous. <Subject 1> (S1), speaking off-screen from the established scene, continues seamlessly across the cut with <d>[Chinese] <scenetrans>密码是你生日。<scenetrans></d>. Delivery: same continuous voice, softening on her birthday. Sound: Her voice crosses the cut without a restart; fingertips leave the tabletop quietly.
[Shot 3] At 00:04.900, Cut back to a waist-up two-shot of <Subject 1> and <Subject 2>, keeping the card between them at the bottom of frame. Mother releases all contact with it and directs the help toward the operation; the daughter's hand starts forward, then stops before touching it. Hold both faces so the sacrifice and refusal develop together. <Subject 1> (S1), continues seamlessly across the cut with <d>[Chinese] <scenetrans>拿去给你婆婆做手术，该检查就检查，该用药就用药。</d>. Delivery: practical and unwavering, with care in the repeated each necessary step. Sound: The elder's breath and a faint sleeve brush stay close; the music warms under the practical instructions.
[Shot 4] At 00:10.900, Cut on the stopped hand to <Subject 2> in a medium close-up including her palm above the table. She refuses immediately, then draws that palm back toward her own body. End with her tear-bright eyes and the untouched card still visible low in the frame, keeping Mother at the identified right edge. <Subject 2> (S3), in a clear, slightly bright young adult female Mandarin voice, says <d>[Chinese] 不行，这是您的养老钱，我不能拿。</d>. Delivery: startled and urgent, more worried for her mother than argumentative. Sound: The first word enters quickly; the refusal ends over a shaky inhale.
overall_soundscape: Quiet home room tone with only the specified footsteps, fabric and prop sounds; each line belongs to its named speaker and other visible characters listen with closed lips.
non_diegetic_music: Warm, restrained piano, easing gradually as the relationship softens.```

## 样例：原第13组

温情：女儿从对面绕到母亲身旁，横移以二人处于同侧为终点，关系变化可见。

参考图依次：
- `assets\丈母娘_粉衣绿马甲.png`
- `assets\芝夏_米色外套.png`
- `assets\家中客厅与玄关.png`

继承上一镜尾帧：否。

完整提示词：

```text
subject_definitions:
<Subject 1> is Zhixia's mother and Mingyuan's mother-in-law, about sixty, with short gray-black curls, a pink long-sleeved top under a dark green vest, and dark trousers, from <Picture 1>.
<Subject 2> is Zhixia, about thirty, with straight shoulder-length black hair, a beige short trench-style jacket over a gray collared top, and light trousers; her brown shoulder bag is a removable scene prop, from <Picture 2>.
<Subject 3> is the consistent modern home interior with a pale sofa, wooden coffee table and TV console, a dark entry door, and a clear route between living room and entry; use the room layout and daylight only, with people supplied separately, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 live-action family-drama sequence. The daughter admits her mistake and moves from an opposing stance to sitting beside her mother.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain identity, hair and clothing; physical expression and blocking follow the scene.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain the home layout, furniture and daylight in the home shots.
detailed_description: Photorealistic contemporary Chinese family drama, natural skin texture and consistent soft daylight mixed with warm room light. Play the dialogue as continuous human exchanges with actions underneath, keeping speaker voices stable. Current state: Zhixia still stands at the left of the table facing Mother on the sofa right. The brown shoulder bag is on Zhixia, and the card remains untouched on the table.
[Shot 1] Begin with <Subject 2> in medium close-up. She looks from the card to her mother and admits the mistake without hiding behind the earlier argument. Keep the camera steady while the raised chin drops and the grip on the strap releases. <Subject 2> (S3), in a clear, slightly bright young adult female Mandarin voice, says <d>[Chinese] 妈，是我钻牛角尖了。<scenetrans></d>. Delivery: honest and tearful, one small catch before admitting fault. Sound: Her breath is audible, but the words follow without a long sobbing gap.
[Shot 2] At 00:04.000, Cut to a medium-wide relation shot as <Subject 2> removes the brown shoulder bag, places it on the sofa arm, and moves around the open end of the table to sit near <Subject 1> while finishing the same thought. Make one short lateral move with her crossing; end with both women on the same side of the frame and the card in front of them. <Subject 2> (S3), continues seamlessly across the cut with <d>[Chinese] <scenetrans>我只记着自己受的委屈，却忘了明远这些年受的累。</d>. Delivery: remorseful but intelligible, spoken through the purposeful move to sit. Sound: The strap settles, a footstep passes the table and the sofa cushion compresses under the continuous voice.
[Shot 3] At 00:09.100, Hold a seated two-shot at eye level. <Subject 1> turns toward <Subject 2> and answers without lecturing down at her; the daughter meets her eyes and begins to straighten with a decision. Keep their closeness visible and end on that readiness to act. <Subject 1> (S1), in a slightly husky, direct older female Mandarin voice, says <d>[Chinese] 一家人过日子，不怕吃点亏，就怕人人都只算自己的账。</d>. Delivery: gentle and plainspoken, stressing being one family and counting only one's own costs. Sound: Soft room tone and a quiet sleeve movement replace the earlier tense pulse.
overall_soundscape: Quiet home room tone with only the specified footsteps, fabric and prop sounds; each line belongs to its named speaker and other visible characters listen with closed lips.
non_diegetic_music: Warm, restrained piano, easing gradually as the relationship softens.```

## 新增教学样例：信息揭示驱动镜头

**新增教学样例，非既有用户验收成片。** 本例用于演示先确定信息归属和人物目标，再选择表演方式；不把减少肢体动作当成新的全片风格。

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

完整提示词：

```text
subject_definitions:
<Subject 1> is Lin Qing, a young adult Chinese woman with shoulder-length black hair and a cream knit sweater, from <Picture 1>.
<Subject 2> is Aunt Zhao, an older Chinese woman with short gray-black hair and a dark-blue blouse, from <Picture 2>.
<Subject 3> is the established modest living room with two chairs beside a window and soft afternoon daylight; use its layout and light, with the two people supplied separately, from <Picture 3>.
summary: [reference generation] A 15-second, vertical 9:16 photorealistic live-action Chinese family-drama sequence. An identifying detail reveals a personal sacrifice; Lin Qing challenges the concealment, and Aunt Zhao names a written source for the account.
retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - retain identity, hair and clothing; her expression follows the disclosure.
<Subject 2> (appears in [Shot 1], [Shot 3]): fully_preserved - retain identity, hair and clothing; her delivery shifts from careful disclosure to a direct answer.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - retain chair positions, window direction and afternoon daylight.
detailed_description: Natural skin texture, plausible motion and consistent eyelines. Current state: <Subject 1> sits frame left facing <Subject 2> on the right, both already in conversation in <Subject 3>. Lin Qing's absent older brother is the person whose identifying scar is being discussed. Her father's diary is an existing record to be consulted after this conversation. Voice roster: Lin Qing is S2; Aunt Zhao is S5.
[Shot 1] Begin with a steady seated waist-up two-shot, <Subject 1> left and <Subject 2> right. <Subject 2> addresses Lin Qing directly; the explanation becomes personal on the final clause. <Subject 1>'s attentive expression tightens as she realizes she was involved, and she meets Zhao's eyes. Keep both faces readable. <Subject 2> (S5), in a low, slightly husky older female Mandarin voice, says <d>[Chinese] 你哥哥右手腕有一道旧疤，是小时候救你留下的。</d>. Delivery: measured at first, then more deliberate and emotionally exposed on the final clause. Cut when that revelation turns Lin Qing's listening into a question.
[Shot 2] At 00:04.800, Cut to a clean medium close-up of <Subject 1>, maintaining her look toward frame right. She challenges Zhao immediately, her voice rising on the question before hurt catches up with her anger. Hold the camera steady through the shift; she maintains eye contact with Zhao at the end of the question. <Subject 1> (S2), in a clear young adult female Mandarin voice, says <d>[Chinese] 您以前怎么从来没跟我说过？</d>. Delivery: a quick attack on the withheld truth, stressing that Zhao had never told her, with a briefly uneven breath at the end. Her finishing breath bridges the cut to Zhao's answer.
[Shot 3] At 00:08.200, Cut to a clean medium close-up of <Subject 2>, looking toward frame left. She accepts the accusation before answering. As her reply moves from her own fear to the available written account, make one short, slow push toward her face and stop in a close-up. <Subject 2> (S5), in the same older female Mandarin voice, says <d>[Chinese] 我怕你自责。你父亲当年的日记里，把那天的事记得清清楚楚。</d>. Delivery: exposed and quieter in the first sentence, then firm and precise about the source, with a short natural breath between sentences. Let the final words complete the movement within the 15-second group; her sustained eyeline offers Lin Qing a way to verify the account.
overall_soundscape: Soft living-room tone under continuous turn-taking; each line belongs to its named speaker. Lin Qing's uneven finishing breath connects her question to Zhao's answer. The listener's lips stay closed during the other person's speech.
non_diegetic_music: A faint sustained piano tone beneath the first disclosure, fading under Lin Qing's question so the answer remains exposed.
```

本例的镜头任务由“消息如何改变眼前两人的交流”决定，而不是给旧疤安排触摸动作、给日记安排临时翻找。需要强动作的原稿仍应完整保留强动作；本例不能反向用作删掉争抢、拦阻、拥抱或证据交接的理由。
