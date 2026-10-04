# 用户认可的完整行样例

这些来自《丈母娘拦女婿送冻饺子》的实际交付。学习字段、绑定、动作/声音细节与镜头起落，不迁移人物、台词、商品、28组或7分钟总长。样例时间点只服务该段内容，新剧本逐镜重算。每个样例均为15秒。

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
