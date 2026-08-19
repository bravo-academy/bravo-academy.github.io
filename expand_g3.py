#!/usr/bin/env python3
import json, os
from pathlib import Path
ROOT = Path("/tmp/repo")
# Helper to write lesson
def write_lesson(subject, stem, data):
    p = ROOT / f"levels/g3/{subject}/lessons/{stem}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", p)

# MATH 01 - numbers
write_lesson("math","01_numbers",{
  "title":"الأعداد من 4 و 5 أرقام",
  "episode":"1",
  "brand":"السنة الثالثة أساسي · رياضيات",
  "level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الأعداد من 4 و 5 أرقام حتى 99 999 | رياضيات السنة الثالثة أساسي — الحلقة 1 🔢","tags":"السنة الثالثة أساسي, رياضيات, الأعداد"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"مرحبا يا أبطال الرياضيات!","board_title":"مقدّمة","lines":[{"text":"مرحبا في عالم الأعداد الكبيرة!","style":"small"},{"text":"حتى 99 999","style":"eq"}],"narration":"مرحبا يا أبطال برافو أكاديمي! أنا فرحانة بوجودكم اليوم. تخيّلوا أننا في سوق صفاقس، ونعدّ صناديق الزيتون. هل نستطيع قراءة تسعة وتسعين ألفا؟ هيا ننطلق خطوة بخطوة."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s2.jpg","caption":"منازل الأعداد","board_title":"المنازل","lines":[{"text":"54 872","style":"eq"},{"text":"5 عشرات آلاف · 4 آلاف","style":"small"},{"text":"8 مئات · 7 عشرات · 2 آحاد","style":"label"}],"narration":"انظروا إلى هذا العدد: أربعة وخمسون ألفا وثمانمائة واثنان وسبعون. كل رقم له منزل: الآحاد والعشرات والمئات والآلاف وعشرات الآلاف. الخمسة في منزلة عشرات الآلاف تساوي خمسين ألفا."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s3.jpg","caption":"مثال تونسي","board_title":"مثال","lines":[{"text":"72 350 = 70 000 + 2 000 + 300 + 50","style":"eq"},{"text":"سكان مدينة نابل مثلا","style":"small"}],"narration":"مثال من تونس: نكتب العدد اثنين وسبعين ألفا وثلاثمائة وخمسين. نفكّكه: سبعون ألفا زائد ألفين زائد ثلاثمائة زائد خمسين. هكذا نفهم قيمة كل رقم."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s1.jpg","caption":"نقارن بذكاء","board_title":"مقارنة","lines":[{"text":"45 000  و  9 800","style":"eq"},{"text":"من له منازل أكثر هو الأكبر","style":"op"},{"text":"45 000 > 9 800","style":"answer"}],"narration":"قاعدة ذهبية للمقارنة: نعدّ المنازل أولا. العدد بخمس منازل أكبر من العدد بأربع منازل دائما. لذلك خمسة وأربعون ألفا أكبر من تسعة آلاف وثمانمائة. ولو تساوت المنازل، نقارن خانة بخانة من اليسار."},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s2.jpg","caption":"فكّر قليلا...","board_title":"كويز","lines":[{"text":"رتّب تصاعديا: 8 990 ، 54 872 ، 9 800","style":"ask"},{"text":"... فكّر 3 ثوان ...","style":"label"},{"text":"8 990 < 9 800 < 54 872","style":"answer"}],"narration":"كويز تفاعلي: رتّبوا هذه الأعداد تصاعديا: ثمانية آلاف وتسعمائة وتسعون، تسعة آلاف وثمانمائة، أربعة وخمسون ألفا وثمانمائة واثنان وسبعون. خذوا ثلاث ثوان للتفكير... الجواب: ثمانية آلاف وتسعمائة وتسعون هو الأصغر، ثم تسعة آلاف وثمانمائة، ثم أربعة وخمسون ألفا. هل أصبتم؟","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو يا بطل!","board_title":"برافو!","lines":[{"text":"اكتب بالأرقام: سبعون ألفا وخمسة","style":"ask"},{"text":"أرسل الجواب في التعليقات","style":"label"},{"text":"أنت نجم الرياضيات!","style":"small"}],"narration":"خاتمة مشجعة: تمرين الدار، اكتبوا بالأرقام: سبعون ألفا وخمسة. انتبهوا للأصفار في الوسط! اكتبوا الجواب في التعليقات، وسأصحّح لكم. أنتم أبطال برافو أكاديمي، برافو!","confetti":True}
  ]
})

write_lesson("math","02_ops",{
  "title":"الجمع بالاحتفاظ والطرح بالاستعارة",
  "episode":"2","brand":"السنة الثالثة أساسي · رياضيات","level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الجمع بالاحتفاظ والطرح بالاستعارة | رياضيات الثالثة أساسي — الحلقة 2","tags":"جمع, طرح, Bravo Academy"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/02_s1.jpg","caption":"قصة عم صالح في السوق","board_title":"قصة","lines":[{"text":"في سوق القيروان","style":"small"},{"text":"3 500 + 2 750","style":"eq"}],"narration":"مرحبا يا شطّار! تخيّلوا عم صالح بائع التمور في سوق القيروان. باع في الصباح ثلاثة آلاف وخمسمائة مليم، وفي المساء ألفين وسبعمائة وخمسين. كم باع في اليوم كله؟ نحتاج الجمع بالاحتفاظ."},
    {"audio":"../audio/02_s2.mp3","image":"../img/02_s1.jpg","caption":"خانة بخانة","board_title":"جمع","lines":[{"text":"3 500 + 2 750 = 6 250","style":"eq"},{"text":"من اليمين ونحتفظ بالعشرة","style":"label"}],"narration":"نجمع خانة بخانة من اليمين: صفر زائد صفر صفر، صفر زائد خمسة خمسة، خمسة زائد سبعة اثنا عشر نكتب اثنين ونحتفظ بواحد، ثلاثة زائد اثنين زائد المحفوظ واحد يساوي ستة. الناتج ستة آلاف ومائتان وخمسون."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s3.jpg","caption":"الاستعارة مثل الجار الكريم","board_title":"طرح","lines":[{"text":"6 250 − 2 750 = 3 500","style":"eq"},{"text":"نستعير 1 من الجار","style":"small"}],"narration":"الآن الطرح بالاستعارة: ستة آلاف ومائتان وخمسون ناقص ألفين وسبعمائة وخمسين. إذا كان الرقم فوق صغيرا نستعير واحدا من الجار الكريم على اليسار. الناتج ثلاثة آلاف وخمسمائة."},
    {"audio":"../audio/02_s4.mp3","image":"../img/02_s1.jpg","caption":"مثال سريع","board_title":"مثال","lines":[{"text":"4 680 + 2 540 = 7 220","style":"eq"},{"text":"4 680 − 2 540 = 2 140","style":"op"}],"narration":"مثال سريع: أربعة آلاف وستمائة وثمانون زائد ألفين وخمسمائة وأربعين يساوي سبعة آلاف ومائتين وعشرين. ونفس العددين طرحا يساوي ألفين ومائة وأربعين. لاحظوا الاحتفاظ والاستعارة."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s2.jpg","caption":"فكّر قبل الإجابة","board_title":"كويز","lines":[{"text":"5 125 + 3 876 = ؟","style":"ask"},{"text":"مهلة تفكير 3 ثوان","style":"label"},{"text":"9 001","style":"answer"}],"narration":"كويز: خمسة آلاف ومائة وخمسة وعشرون زائد ثلاثة آلاف وثمانمائة وستة وسبعون كم؟ فكّروا ثلاث ثوان... خمسة زائد ستة أحد عشر نحتفظ، وهكذا حتى نصل إلى تسعة آلاف وواحد. أحسنتم!","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تمارين الدار","lines":[{"text":"6 000 − 3 450 = ؟","style":"ask"},{"text":"اكتب الجواب وطريقة الاستعارة","style":"small"}],"narration":"تمرين الدار: ستة آلاف ناقص ثلاثة آلاف وأربعمائة وخمسون. اكتبوا الحل خطوة بخطوة في التعليقات. أنتم عباقرة الحساب، برافو!","confetti":True}
  ]
})

write_lesson("math","03_geo",{
  "title":"التوازي والتعامد ومحيط المستطيل","episode":"3","brand":"السنة الثالثة أساسي · هندسة","level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"التوازي والتعامد ومحيط المستطيل | هندسة الثالثة أساسي","tags":"هندسة, توازي"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/03_s1.jpg","caption":"سكة قطار تونس","board_title":"مقدّمة","lines":[{"text":"هل رأيت سكة القطار؟","style":"small"},{"text":"خطّان لا يلتقيان أبدا","style":"eq"}],"narration":"أهلا بكم يا مهندسي المستقبل! هل رأيتم سكة قطار تونس من تونس إلى سوسة؟ الخطان يسيران جنبا إلى جنب ولا يلتقيان أبدا مهما طالا. هذا هو التوازي!"},
    {"audio":"../audio/03_s2.mp3","image":"../img/03_s1.jpg","caption":"رمز التوازي","board_title":"توازي //","lines":[{"text":"مستقيمان متوازيان //","style":"eq"},{"text":"المسافة بينهما ثابتة","style":"label"}],"narration":"نرسم مستقيمان متوازيان ونرمز لهما بخطين مائلين. المسافة بينهما ثابتة في كل مكان. مثال: حافّتا كتابكم متوازيتان، وحافّتا السبورة كذلك."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s3.jpg","caption":"الزاوية القائمة","board_title":"تعامد ⊥","lines":[{"text":"يتقاطعان ويصنعان 90°","style":"eq"},{"text":"نتحقّق بالكوس","style":"op"}],"narration":"أما التعامد فهو تقاطع يصنع زاوية قائمة تسعين درجة مثل زاوية باب قسمكم. نتحقق بالكوس المدرسي. نرسم ⊥ للتعامد. مثال: شباك سيدي بوسعيد الأزرق فيه تعامد جميل."},
    {"audio":"../audio/03_s4.mp3","image":"../img/03_s1.jpg","caption":"محيط المستطيل","board_title":"المحيط","lines":[{"text":"P = 2 × (L + l)","style":"eq"},{"text":"L=12m و l=8m → P=40m","style":"answer"}],"narration":"الآن محيط المستطيل. المحيط هو طول السياج حول الجنان. القانون: اثنان في الطول زائد العرض. جنان طوله اثنا عشر مترا وعرضه ثمانية أمتار، محيطه اثنان في عشرين يساوي أربعين مترا."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s2.jpg","caption":"فكّر","board_title":"كويز","lines":[{"text":"مستطيل L=15 و l=10 كم محيطه؟","style":"ask"},{"text":"... 3 ثوان ...","style":"label"},{"text":"P=50","style":"answer"}],"narration":"كويز: مستطيل طوله خمسة عشر وعرضه عشرة، كم محيطه؟ فكروا ثلاث ثوان... نجمع خمسة عشر زائد عشرة خمسة وعشرون في اثنين يساوي خمسين. ممتاز!","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تحدّي","lines":[{"text":"ارسم مستطيلا ومربّعا","style":"ask"},{"text":"حدّد المتوازي والمتعامد","style":"small"}],"narration":"تحدي الدار: ارسموا في كراسكم مستطيلا وحددوا باللون الأزرق الضلعين المتوازيين وبالأحمر الضلعين المتعامدين. صوّروا وشاركونا. برافو يا مهندسين!","confetti":True}
  ]
})

write_lesson("math","04_mult",{
  "title":"جدول الضرب والتمهيد للقسمة","episode":"4","brand":"السنة الثالثة أساسي · رياضيات","level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"جدول الضرب والتمهيد للقسمة | رياضيات الثالثة أساسي","tags":"ضرب, قسمة"},
  "scenes":[
    {"audio":"../audio/04_s1.mp3","image":"../img/04_s1.jpg","caption":"كرتونة البيض","board_title":"الضرب","lines":[{"text":"الضرب = جمع متكرّر","style":"label"},{"text":"2 × 6 = 12","style":"eq"}],"narration":"مرحبا يا أبطال! هل اشتريتم كرتونة بيض من سوق الحلفاوين؟ فيها صفّان كل صف ست بيضات. بدل أن نجمع ستة زائد ستة، نقول اثنان في ستة يساوي اثني عشر. الضرب يختصر الجمع المتكرر."},
    {"audio":"../audio/04_s2.mp3","image":"../img/04_s1.jpg","caption":"جدول الثلاثة","board_title":"جدول","lines":[{"text":"3×1=3  3×2=6  3×3=9","style":"eq"},{"text":"3×4=12  3×5=15","style":"op"}],"narration":"نحفظ جدول الثلاثة معا: ثلاثة في واحد ثلاثة، ثلاثة في اثنين ستة، ثلاثة في ثلاثة تسعة، ثلاثة في أربعة اثنا عشر، ثلاثة في خمسة خمسة عشر. غنّوها معي بإيقاع."},
    {"audio":"../audio/04_s3.mp3","image":"../img/01_s2.jpg","caption":"خاصية التبديل","board_title":"خاصية","lines":[{"text":"3 × 4 = 4 × 3","style":"eq"},{"text":"النتيجة واحدة","style":"label"}],"narration":"خاصية جميلة: التبديل لا يغيّر النتيجة. ثلاثة في أربعة تساوي أربعة في ثلاثة وكلاهما اثنا عشر. هذا يسهّل الحفظ، احفظوا نصف الجدول فقط!"},
    {"audio":"../audio/04_s4.mp3","image":"../img/01_s3.jpg","caption":"القسمة عكس الضرب","board_title":"قسمة","lines":[{"text":"12 ÷ 4 = 3","style":"eq"},{"text":"لأن 3 × 4 = 12","style":"small"}],"narration":"القسمة عكس الضرب. إذا كان عندنا اثنتا عشرة حلوى ونوزعها على أربعة أصدقاء بالتساوي، كم لكل واحد؟ اثنتا عشرة تقسيم أربعة تساوي ثلاثة، لأن ثلاثة في أربعة اثنا عشر."},
    {"audio":"../audio/04_s5.mp3","image":"../img/04_s1.jpg","caption":"كويز الفرّان","board_title":"كويز","lines":[{"text":"فكّر: 7 × 5 = ؟  و 35 ÷ 5 = ؟","style":"ask"},{"text":"... مهلة ...","style":"label"},{"text":"35  و  7","style":"answer"}],"narration":"كويز الفرّان في سيدي بوسعيد: سبعة في خمسة كم؟ و خمسة وثلاثون تقسيم خمسة كم؟ فكروا... سبعة في خمسة خمسة وثلاثون، وخمسة وثلاثون تقسيم خمسة سبعة. ممتاز!","pause_after":2},
    {"audio":"../audio/04_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تحدّي","lines":[{"text":"احفظ جدول 6","style":"ask"},{"text":"وحل 5×6 و 18÷3","style":"small"}],"narration":"تحدي الدار: احفظوا جدول ستة، وحلّوا خمسة في ستة وثمانية عشر تقسيم ثلاثة في التعليقات. أنتم نجوم الضرب، برافو!","confetti":True}
  ]
})

write_lesson("math","05_fractions",{
  "title":"الكسور البسيطة","episode":"5","brand":"السنة الثالثة أساسي · رياضيات","level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الكسور البسيطة | رياضيات الثالثة أساسي 🍕","tags":"كسور"},
  "scenes":[
    {"audio":"../audio/05_s1.mp3","image":"../img/01_s3.jpg","caption":"بيتزا القيروان","board_title":"مقدّمة","lines":[{"text":"قسّمنا بيتزا إلى 4","style":"small"},{"text":"قطعة واحدة = 1/4","style":"eq"}],"narration":"مرحبا يا عشاق البيتزا! قسّمنا بيتزا القيروان إلى أربعة أجزاء متساوية وأخذنا قطعة واحدة. هذه القطعة هي ربع البيتزا، نكتبها واحد على أربعة."},
    {"audio":"../audio/05_s2.mp3","image":"../img/02_s1.jpg","caption":"بسط ومقام","board_title":"مفهوم","lines":[{"text":"البسط فوق","style":"label"},{"text":"المقام تحت → عدد القطع الكلّي","style":"small"},{"text":"1 / 4","style":"eq"}],"narration":"الكسر له بسط فوق ومقام تحت والخط بينهما. المقام يقول كم قطعة قسّمنا الكل، والبسط يقول كم أخذنا. في الربع، المقام أربعة والبسط واحد."},
    {"audio":"../audio/05_s3.mp3","image":"../img/03_s1.jpg","caption":"أيهما أكبر؟","board_title":"مقارنة","lines":[{"text":"1/2 > 1/4","style":"eq"},{"text":"النصف أكبر من الربع","style":"answer"}],"narration":"أيهما أكبر نصف كعكة العيد أم ربعها؟ بالطبع النصف أكبر. قاعدة: إذا كان البسط نفسه، فالمقام الأصغر يعطي قطعة أكبر. نصف أكبر من ربع وثلث أكبر من سدس."},
    {"audio":"../audio/05_s4.mp3","image":"../img/02_s1.jpg","caption":"نلوّن ونجمع","board_title":"نشاط","lines":[{"text":"1/4 + 1/4 = 2/4 = 1/2","style":"eq"},{"text":"ربوعان = نصف","style":"label"}],"narration":"لو جمعنا ربعين نحصل على نصف. ارسموا دائرة، لونوا ربعا ثم ربعا آخر، سترون أن الملون هو النصف. الكسور ليست صعبة، إنها تلوين ومرح!"},
    {"audio":"../audio/05_s5.mp3","image":"../img/01_s2.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"أيهما أكبر: 1/3 أم 1/6 ؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"1/3 > 1/6","style":"answer"}],"narration":"كويز: أيهما أكبر ثلث البقلاوة أم سدسها؟ فكّروا ثلاث ثوان... الثلث أكبر لأن ثلاثة أصغر من ستة في المقام، والقطعة تكون أكبر. هل عرفتم؟","pause_after":2},
    {"audio":"../audio/05_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"برافو!","lines":[{"text":"ارسم دائرة وقسّمها إلى 8","style":"ask"},{"text":"لوّن 3/8 وشارك الصورة","style":"small"}],"narration":"تمرين الدار: ارسموا دائرة وقسّموها إلى ثمانية أجزاء متساوية ولونوا ثلاثة أثمان. اكتبوا الكسر وشاركوا الرسمة. برافو يا فناني الكسور!","confetti":True}
  ]
})

write_lesson("math","06_measures",{
  "title":"قياس الأطوال والكتل","episode":"6","brand":"السنة الثالثة أساسي · رياضيات","level":"g3","subject":"math","width":1920,"height":1080,"fps":24,
  "yt":{"title":"قياس الأطوال والكتل | رياضيات الثالثة أساسي 📏","tags":"قياس"},
  "scenes":[
    {"audio":"../audio/06_s1.mp3","image":"../img/03_s1.jpg","caption":"نقيس بالمسطرة","board_title":"الأطوال","lines":[{"text":"1 m = 100 cm","style":"eq"},{"text":"1 km = 1000 m","style":"op"}],"narration":"مرحبا يا قياسي المستقبل! نقيس الأطوال بالمتر والسنتيمتر. المسطرة فيها ثلاثون سنتيمترا. المتر يساوي مئة سنتيمتر، والكيلومتر يساوي ألف متر مثل المسافة بين مدنين وحومتين."},
    {"audio":"../audio/06_s2.mp3","image":"../img/01_s2.jpg","caption":"كيس السكر","board_title":"الكتل","lines":[{"text":"1 kg = 1000 g","style":"eq"},{"text":"كيس سكر = 1 كغ","style":"small"}],"narration":"الكتلة هي الوزن. نزنها بالميزان. كيس السكر وزنه كيلوغرام واحد يساوي ألف غرام. نصف كيلو خبز يساوي خمسمائة غرام. في سوق المنزه نزن الغلال بالكيلوغرام."},
    {"audio":"../audio/06_s3.mp3","image":"../img/01_s1.jpg","caption":"التحويل","board_title":"تحويل","lines":[{"text":"2500 g = 2 kg و 500 g","style":"eq"},{"text":"350 cm = 3 m و 50 cm","style":"op"}],"narration":"التحويل سهل: ألفان وخمسمائة غرام تساوي كيلوغرامين وخمسمائة غرام. وثلاثمائة وخمسون سنتيمترا تساوي ثلاثة أمتار وخمسين سنتيمترا. نحول لنفهم."},
    {"audio":"../audio/06_s4.mp3","image":"../img/02_s1.jpg","caption":"مثال حي","board_title":"مثال","lines":[{"text":"طاولة 120 cm = 1 m 20 cm","style":"eq"},{"text":"قارورة 1.5 L","style":"label"}],"narration":"مثال حي: طاولة قسمكم طولها مئة وعشرون سنتيمترا، أي متر وعشرون سنتيمترا. وقارورة الماء لتر ونصف. القياسات في كل مكان حولنا، حتى ملعب الكرة."},
    {"audio":"../audio/06_s5.mp3","image":"../img/03_s1.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"كم غراما في نصف كيلو + ربع كيلو؟","style":"ask"},{"text":"مهلة تفكير","style":"label"},{"text":"500+250=750 g","style":"answer"}],"narration":"كويز: نصف كيلو خمسمائة غرام، وربع كيلو مئتان وخمسون غراما. كم مجموعهما؟ فكروا... خمسمائة زائد مئتين وخمسين يساوي سبعمائة وخمسين غراما. برافو!","pause_after":2},
    {"audio":"../audio/06_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"برافو!","lines":[{"text":"زن وزنك وطولك","style":"ask"},{"text":"اكتب: أنا وزني ... وطولي ...","style":"small"}],"narration":"تمرين الدار: قس طولك بالسنتيمتر ووزنك بالكيلوغرام بمساعدة وليّك واكتب الجملة: أنا طولي كذا ووزني كذا. شاركونا. أنتم أبطال القياس، برافو!","confetti":True}
  ]
})

# ARABIC
write_lesson("arabic","01_jumla",{
  "title":"الجملة الفعلية والجملة الاسمية","episode":"1","brand":"السنة الثالثة أساسي · لغة عربية","level":"g3","subject":"arabic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الجملة الفعلية والاسمية | عربية السنة الثالثة — الحلقة 1 ✏️"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"مرحبا يا كتّاب المستقبل","board_title":"مقدمة","lines":[{"text":"هل تحبّون تكوين الجمل؟","style":"small"},{"text":"اليوم سرّ الجملة!","style":"eq"}],"narration":"مرحبا يا كتّاب المستقبل في برافو أكاديمي! هل سألتم أنفسكم كيف نميز الجمل في كتاب القراءة؟ اليوم نكشف سرّا بسيطا يجعلكم أذكياء في العربية."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s1.jpg","caption":"فعلية","board_title":"جملة فعلية","lines":[{"text":"يلعبُ سامي بالكرة","style":"eq"},{"text":"فعل + فاعل + مفعول","style":"label"}],"narration":"الجملة الفعلية تبدأ بفعل. انظروا: يلعب سامي بالكرة. يلعب فعل مضارع، وسامي فاعل، وبالكرة جار ومجرور. أول كلمة هي السر، إذا كانت فعلا فالجملة فعلية."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s2.jpg","caption":"اسمية","board_title":"جملة اسمية","lines":[{"text":"الكتابُ ممتعٌ","style":"eq"},{"text":"مبتدأ + خبر","style":"label"}],"narration":"أما الجملة الاسمية فتبدأ باسم. مثال: الكتاب ممتع. الكتاب مبتدأ مرفوع، وممتع خبر مرفوع. لا يوجد فعل في أولها، بل اسم واضح."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s2.jpg","caption":"ميزان سريع","board_title":"تمييز","lines":[{"text":"يشرح المعلمُ ↔ المعلّمُ نشيطٌ","style":"op"},{"text":"فعلية  و  اسمية","style":"answer"}],"narration":"ميزان سريع: يشرح المعلم الدرس جملة فعلية لأنها بدأت بالفعل يشرح. والمعلم نشيط جملة اسمية لأنها بدأت بالاسم المعلم. هل لاحظتم الفرق؟"},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s3.jpg","caption":"فكّر","board_title":"كويز","lines":[{"text":"ينجح المجتهدُ — فعلية أم اسمية؟","style":"ask"},{"text":"... فكّر 3 ثوان ...","style":"label"},{"text":"فعلية (تبدأ بـ ينجح)","style":"answer"}],"narration":"كويز: ينجح المجتهد، فعلية أم اسمية؟ فكروا ثلاث ثوان... الجواب فعلية لأنها بدأت بالفعل ينجح. لو قلنا المجتهد ناجح تصبح اسمية. أحسنتم!","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"إنتاج","lines":[{"text":"اكتب جملة فعلية واسمية عن المدرسة","style":"ask"},{"text":"شارك في التعليقات","style":"small"}],"narration":"تمرين الدار: اكتبوا جملة فعلية وجملة اسمية عن مدرستكم الجميلة في بنزرت أو قفصة. مثلا: تفتح المدرسة أبوابها، والمدرسة نظيفة. أنتم مبدعون، برافو!","confetti":True}
  ]
})

write_lesson("arabic","02_sarf",{
  "title":"تصريف الأفعال في الماضي والحاضر","episode":"2","brand":"السنة الثالثة أساسي · لغة عربية","level":"g3","subject":"arabic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"تصريف الماضي والحاضر | عربية الثالثة"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/01_s1.jpg","caption":"أمس واليوم","board_title":"زمن الفعل","lines":[{"text":"أمس: كتبَ","style":"label"},{"text":"اليوم: يكتبُ","style":"eq"}],"narration":"مرحبا يا صرفيين! الفعل يعيش في الزمن. أمس نقول كتبَ وانتهى، واليوم نقول يكتبُ وما زال يكتب. الماضي يبدأ غالبا بفتحة، والحاضر يبدأ بحرف من أنيت: أكتب نكتب يكتب تكتب."},
    {"audio":"../audio/02_s2.mp3","image":"../img/01_s2.jpg","caption":"مع أنا ونحن","board_title":"ضمائر","lines":[{"text":"أنا أكتبُ · نحن نكتبُ","style":"small"},{"text":"أنا كتبتُ · نحن كتبنا","style":"op"}],"narration":"مع الضمائر: في الحاضر نقول أنا أكتب ونحن نكتب، وفي الماضي أنا كتبت ونحن كتبنا. لاحظوا تغير الحروف في أول الفعل وآخره."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s1.jpg","caption":"هو وهي","board_title":"هو / هي","lines":[{"text":"هو يكتبُ · هي تكتبُ","style":"eq"},{"text":"هو كتبَ · هي كتبتْ","style":"small"}],"narration":"هو يكتب وهي تكتب في الحاضر، وتاء التأنيث تظهر في هي. وفي الماضي: هو كتب وهي كتبت بإضافة تاء في الآخر. هذه التاء علامة المؤنث."},
    {"audio":"../audio/02_s4.mp3","image":"../img/01_s2.jpg","caption":"مثال تونسي","board_title":"مثال","lines":[{"text":"زرع الفلّاحُ → يزرع الفلّاحُ","style":"eq"},{"text":"في حقول باجة","style":"small"}],"narration":"مثال تونسي جميل: في الماضي نقول زرع الفلاح القمح في حقول باجة، وفي الحاضر نقول يزرع الفلاح القمح. نفس الفعل، زمن مختلف. جربوا مع زرع."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"صرّف: قرأ → أنا وهو في الحاضر؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"أنا أقرأ · هو يقرأ","style":"answer"}],"narration":"كويز: صرّفوا الفعل قرأ في الحاضر مع أنا وهو. فكّروا ثلاث ثوان... أنا أقرأ كتابا وهو يقرأ كتابا. هل كتبتموها صحيحة؟","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تمرين","lines":[{"text":"صرّف: لعب مع هي ونحن","style":"ask"},{"text":"ماض وحاضر","style":"small"}],"narration":"تمرين الدار: صرفوا الفعل لعب في الماضي والحاضر مع هي ونحن. اكتبوا أربع جمل في التعليقات. أنتم أبطال الصرف، برافو!","confetti":True}
  ]
})

write_lesson("arabic","03_punct",{
  "title":"علامات الترقيم والإنتاج الكتابي","episode":"3","brand":"السنة الثالثة أساسي · لغة عربية","level":"g3","subject":"arabic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"علامات الترقيم | عربية الثالثة"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/01_s2.jpg","caption":"إشارات المرور للكلام","board_title":"لماذا؟","lines":[{"text":"بدونها يضيع المعنى!","style":"small"},{"text":". ، ؟ !","style":"eq"}],"narration":"مرحبا يا كتّاب! تخيلوا كلاما بدون إشارات مرور، ستضيع السيارات. كذلك الكتابة بدون علامات ترقيم يضيع المعنى. اليوم نتعلم إشارات الكتابة."},
    {"audio":"../audio/03_s2.mp3","image":"../img/01_s3.jpg","caption":"النقطة والفاصلة","board_title":"علامات","lines":[{"text":" . توقف كامل","style":"label"},{"text":"، استراحة قصيرة","style":"op"}],"narration":"النقطة في آخر الجملة توقف كامل، مثل التوقف عند المدرسة. والفاصلة استراحة قصيرة للتنفس: اشتريت خبزا، وزيتونا، وحليبا. ترتيب وأدب."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s2.jpg","caption":"سؤال وتعجب","board_title":"؟ !","lines":[{"text":"هل تحبّ المدرسة؟","style":"ask"},{"text":"ما أجمل تونس!","style":"eq"}],"narration":"علامة الاستفهام للسؤال: هل تحب المدرسة؟ وعلامة التعجب للدهشة والفرح: ما أجمل علم تونس! ما أروع شط قليبية!"},
    {"audio":"../audio/03_s4.mp3","image":"../img/01_s1.jpg","caption":"فقرة منسّقة","board_title":"إنتاج","lines":[{"text":"فكرة + أمثلة + خاتمة","style":"eq"},{"text":"3 جمل بعلامات صحيحة","style":"small"}],"narration":"كيف نكتب فقرة؟ نبدأ بفكرة: مدرستي جميلة، ثم أمثلة: فيها ساحة واسعة ومكتبة، ونختم بخاتمة: أحب مدرستي كثيرا. ثلاث جمل بعلامات صحيحة، وكفى."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s3.jpg","caption":"صحّح","board_title":"كويز","lines":[{"text":"أين النقطة؟ ذهب أحمد إلى السوق اشترى خبزا","style":"ask"},{"text":"فكّر","style":"label"},{"text":"السوق. اشترى","style":"answer"}],"narration":"كويز صحّح: ذهب أحمد إلى السوق اشترى خبزا. أين نضع النقطة؟ فكروا... بعد كلمة السوق نضع نقطة، لأنها نهاية جملة. ذهب أحمد إلى السوق. اشترى خبزا.","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"برافو!","lines":[{"text":"اكتب 3 جمل عن عائلتك","style":"ask"},{"text":"بـ . ، ؟ !","style":"small"}],"narration":"تمرين الدار: اكتبوا ثلاث جمل عن عائلتكم واستعملوا النقطة والفاصلة وعلامة الاستفهام أو التعجب. أرسلوها وسأصححها لكم. برافو يا كتّاب!","confetti":True}
  ]
})

write_lesson("arabic","04_naat",{
  "title":"النعت والإضافة التمهيدية","episode":"4","brand":"السنة الثالثة أساسي · لغة عربية","level":"g3","subject":"arabic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"النعت والإضافة | عربية الثالثة"},
  "scenes":[
    {"audio":"../audio/04_s1.mp3","image":"../img/01_s2.jpg","caption":"وصف جميل","board_title":"نعت","lines":[{"text":"الكتابُ المفيدُ","style":"eq"},{"text":"المفيد نعت يصف الكتاب","style":"small"}],"narration":"أهلا بكم! النعت كلمة تصف اسما قبلها وتتبعه في الحركة. نقول الكتاب المفيد، المفيد نعت يصف الكتاب ويتبعه في الضمّة. كأننا نلوّن الكتاب بصفة جميلة."},
    {"audio":"../audio/04_s2.mp3","image":"../img/01_s3.jpg","caption":"ألوان النعت","board_title":"أمثلة","lines":[{"text":"الوردةُ الحمراءُ","style":"eq"},{"text":"القمرُ المنيرُ","style":"op"}],"narration":"أمثلة تونسية: الوردة الحمراء في حديقة البلفيدير، والقمر المنير فوق سيدي بوسعيد. الحمراء نعت للوردة، والمنير نعت للقمر. كلاهما مرفوع مثل المنعوت."},
    {"audio":"../audio/04_s3.mp3","image":"../img/01_s1.jpg","caption":"الإضافة","board_title":"إضافة","lines":[{"text":"حقيبةُ التلميذِ","style":"eq"},{"text":"كتابُ القراءةِ","style":"small"}],"narration":"أما الإضافة فتربط اسمين: الثاني يوضح الأول. حقيبة التلميذ، كتاب القراءة، علم تونس. الاسم الثاني مجرور دائما، نقول التلميذ بالكسرة."},
    {"audio":"../audio/04_s4.mp3","image":"../img/01_s2.jpg","caption":"فرق واضح","board_title":"فرق","lines":[{"text":"نعت: يتبع الحركة","style":"label"},{"text":"إضافة: الثاني مجرور","style":"op"}],"narration":"الفرق الواضح: النعت يتبع المنعوت في الحركة إن كان مرفوعا فالنعت مرفوع، أما المضاف إليه فمجرور دائما. هذه القاعدة الذهبية."},
    {"audio":"../audio/04_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"حدّد: كتابُ التلميذِ المجتهدِ","style":"ask"},{"text":"أين النعت وأين الإضافة؟","style":"label"},{"text":"إضافة: كتاب التلميذ / نعت: المجتهد","style":"answer"}],"narration":"كويز: في جملة كتاب التلميذ المجتهد، أين الإضافة وأين النعت؟ فكروا... كتاب التلميذ إضافة، والمجتهد نعت للتلميذ. هل أصبتم؟","pause_after":2},
    {"audio":"../audio/04_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تحدّي","lines":[{"text":"أكمل: القمرُ ...","style":"ask"},{"text":"بنعت وإضافة","style":"small"}],"narration":"تحدي الدار: أكملوا: القمر ... بنعت مناسب، ثم كونوا إضافة عن المدرسة مثل سور المدرسة. اكتبوا في التعليقات، أنتم مبدعون برافو!","confetti":True}
  ]
})

# SCIENCE
write_lesson("science","01_respiration",{
  "title":"التنفس والدوران ومخاطر التلوث","episode":"1","brand":"السنة الثالثة أساسي · إيقاظ علمي","level":"g3","subject":"science","width":1920,"height":1080,"fps":24,
  "yt":{"title":"التنفس والدوران | إيقاظ علمي الثالثة أساسي 🫁"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"شهيق وزفير","board_title":"تنفّس","lines":[{"text":"تتنفس 16 مرة في الدقيقة","style":"eq"},{"text":"شهيق يدخل، زفير يخرج","style":"small"}],"narration":"مرحبا يا علماء المستقبل! ضعوا يدكم على صدركم وتنفسوا. تشهق فيدخل الهواء إلى الرئتين، وتزفر فيخرج. نتنفس نحو ست عشرة مرة في الدقيقة ونحن جالسون."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s2.jpg","caption":"القلب مضخة","board_title":"دوران","lines":[{"text":"90 خفقة في الدقيقة","style":"eq"},{"text":"الدم ينقل الأكسجين","style":"label"}],"narration":"قلبكم مضخة عجيبة تضخ الدم ليلا ونهارا. ينبض نحو تسعين خفقة في الدقيقة عند الأطفال. الدم يحمل الأكسجين من الرئتين إلى كل الجسم."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s1.jpg","caption":"مخاطر تونسية","board_title":"تلوّث","lines":[{"text":"دخان السيارات والمصانع","style":"op"},{"text":"يمرض الرئتين","style":"small"}],"narration":"لكن هواءنا في تونس قد يتلوث بدخان السيارات في تونس العاصمة وبغبار المصانع. التلوث يمرض الرئتين ويجعل التنفس صعبا. حتى حرق البلاستيك خطر."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s2.jpg","caption":"نحمي أنفسنا","board_title":"حماية","lines":[{"text":"أكثر خضرة + رياضة","style":"eq"},{"text":"بعيدا عن الدخان","style":"label"}],"narration":"كيف نحمي أنفسنا؟ نزرع الأشجار، نمارس الرياضة في الهواء النظيف في الحدائق، ونبتعد عن التدخين والغبار. شجرة واحدة تعطي أكسجينا لعائلة كاملة!"},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"90 × 5 دقائق = ؟ خفقة","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"450 خفقة","style":"answer"}],"narration":"كويز حسابي علمي: إذا كان قلبك تسعين خفقة في الدقيقة، كم خفقة في خمس دقائق؟ فكروا ثلاث ثوان... نضرب تسعين في خمسة يساوي أربعمائة وخمسين. ممتاز!","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"ارسم رئة وقلبا","style":"ask"},{"text":"واكتب 3 طرق للحماية","style":"small"}],"narration":"مهمة الدار: ارسم رئة وقلبا واكتب ثلاث طرق تحمي بها تنفسك في حومتك. شارك الرسمة مع عائلتك. أنتم حماة الصحة، برافو!","confetti":True}
  ]
})

write_lesson("science","02_circuit",{
  "title":"الدارة الكهربائية البسيطة","episode":"2","brand":"السنة الثالثة أساسي · إيقاظ علمي","level":"g3","subject":"science","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الدارة الكهربائية البسيطة | إيقاظ علمي الثالثة"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/02_s1.jpg","caption":"من وين يجي الضوء؟","board_title":"مكونات","lines":[{"text":"بطارية + أسلاك + مصباح + قاطعة","style":"eq"}],"narration":"أهلا بالمخترعين! من وين يجي الضو في مصباح الجيب؟ من دارة بسيطة: بطارية صغيرة تعطي الكهرباء، وسلكان ينقلانها، ومصباح يضيء، وقاطعة تفتح وتغلق. كهرباء الدار خطيرة، نستعمل البطارية فقط."},
    {"audio":"../audio/02_s2.mp3","image":"../img/02_s1.jpg","caption":"مغلقة = يضيء","board_title":"مغلقة","lines":[{"text":"دارة مغلقة → يضيء ✨","style":"answer"},{"text":"مسار كامل للتيار","style":"label"}],"narration":"إذا كانت القاطعة مغلقة، يعني المسار كامل والكهرباء تدور في حلقة، يضيء المصباح. مثل طريق دائري بلا انقطاع."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s3.jpg","caption":"مفتوحة = ينطفئ","board_title":"مفتوحة","lines":[{"text":"دارة مفتوحة → ينطفئ","style":"op"},{"text":"انقطع المسار","style":"small"}],"narration":"وإذا فتحنا القاطعة، انقطع الطريق وانطفأ المصباح. هذا هو الفرق بين المفتوحة والمغلقة. جربوها ببطارية لعبة."},
    {"audio":"../audio/02_s4.mp3","image":"../img/02_s1.jpg","caption":"مصباحان","board_title":"توسيع","lines":[{"text":"مصباحان في نفس الدارة","style":"eq"},{"text":"على التوالي","style":"small"}],"narration":"ماذا لو وضعنا مصباحين على التوالي في نفس الدارة؟ يضيئان معا لكن أقل سطوعا، وإذا احترق أحدهما انطفأ الآخر. مثل زينة العيد."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"ما الذي يحدث لو نزعنا البطارية؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"تنطفئ الدارة كلها","style":"answer"}],"narration":"كويز: ماذا يحدث لو نزعنا البطارية من الدارة؟ فكروا ثلاث ثوان... لا مصدر للطاقة، فتنطفئ الدارة كلها. البطارية هي القلب.","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"سلامة","lines":[{"text":"ارسم دارة بمصباحين وقاطعة","style":"ask"},{"text":"لا تلمس كهرباء المنزل!","style":"small"}],"narration":"مهمة الدار: ارسم دارة فيها بطارية ومصباحان وقاطعة، ولوّن مسار التيار. تذكروا لا تلمسوا مقابس المنزل أبدا، الكهرباء المنزلية خطيرة. برافو يا مخترعين!","confetti":True}
  ]
})

write_lesson("science","03_matter",{
  "title":"حالات المادة وتحولاتها","episode":"3","brand":"السنة الثالثة أساسي · إيقاظ علمي","level":"g3","subject":"science","width":1920,"height":1080,"fps":24,
  "yt":{"title":"حالات المادة وتحولاتها | إيقاظ علمي الثالثة"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/03_s1.jpg","caption":"ثلاث حالات","board_title":"المادة","lines":[{"text":"صلب · سائل · غاز","style":"eq"},{"text":"الماء مثال عجيب","style":"small"}],"narration":"مرحبا يا علماء! المادة قد تكون صلبة مثل الحجارة، أو سائلة مثل الماء، أو غازية مثل البخار. والماء وحده يستطيع أن يكون ثلاثتها، عجيب!"},
    {"audio":"../audio/03_s2.mp3","image":"../img/03_s1.jpg","caption":"جليد وماء وبخار","board_title":"الماء","lines":[{"text":"جليد = صلب","style":"label"},{"text":"ماء = سائل · بخار = غاز","style":"op"}],"narration":"في فريزر داركم، الماء يصبح جليدا صلبا. في الحنفية هو سائل. فوق براد الشاي يصعد بخار غازي. نفس المادة، حالات مختلفة حسب الحرارة."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s1.jpg","caption":"انصهار وتجمد","board_title":"تحول1","lines":[{"text":"انصهار عند 0°","style":"eq"},{"text":"تجمد عكسه","style":"op"}],"narration":"التحول الأول: الانصهار. الجليد ينصهر عند صفر درجة ويصبح ماء. والعكس هو التجمد، الماء يتجمد عند صفر ويصبح جليدا."},
    {"audio":"../audio/03_s4.mp3","image":"../img/01_s2.jpg","caption":"تبخر وتكاثف","board_title":"تحول2","lines":[{"text":"تبخر عند 100°","style":"label"},{"text":"تكاثف على المرآة","style":"small"}],"narration":"التحول الثاني: التبخر. الماء يغلي عند مئة درجة ويصبح بخارا. والعكس هو التكاثف، البخار يلمس سطحا باردا فيصبح قطرات، مثل مرآة الحمام بعد الدوش الساخن."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s3.jpg","caption":"فكّر","board_title":"كويز","lines":[{"text":"أين نرى التكاثف في الشتاء؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"على زجاج النافذة","style":"answer"}],"narration":"كويز: أين نرى التكاثف في شتاء تونس البارد؟ فكروا ثلاث ثوان... على زجاج النافذة قطرات ماء، وعلى غطاء طنجرة الكسكسي. أحسنتم!","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"تجربة","lines":[{"text":"ضع مكعب جليد في كأس وراقب","style":"ask"},{"text":"ماذا حدث بعد 10 دقائق؟","style":"small"}],"narration":"تجربة الدار: ضعوا مكعب جليد في كأس وراقبوه عشر دقائق. ماذا حدث؟ اكتبوا: انصهر وأصبح ماء. شاركوا الصورة. برافو يا علماء المادة!","confetti":True}
  ]
})

write_lesson("science","04_food",{
  "title":"التغذية والصحة","episode":"4","brand":"السنة الثالثة أساسي · إيقاظ علمي","level":"g3","subject":"science","width":1920,"height":1080,"fps":24,
  "yt":{"title":"التغذية والصحة | إيقاظ علمي الثالثة"},
  "scenes":[
    {"audio":"../audio/04_s1.mp3","image":"../img/03_s1.jpg","caption":"طبق متوازن","board_title":"غذاء","lines":[{"text":"خضر · غلال · حبوب · ماء","style":"eq"},{"text":"قليل سكر وملح","style":"label"}],"narration":"أهلا بكم يا أبطال الصحة! جسمنا مثل سيارة تحتاج وقودا جيدا. نحتاج كل يوم خضرا مثل السلطة، وغلالا مثل البرتقال، وحبوبا مثل الكسكسي، وماء كثيرا."},
    {"audio":"../audio/04_s2.mp3","image":"../img/02_s1.jpg","caption":"فطور الصباح","board_title":"فطور","lines":[{"text":"حليب + خبز كامل + تمر","style":"eq"},{"text":"طاقة للتركيز","style":"small"}],"narration":"فطور الصباح مهم جدا قبل المدرسة. كأس حليب وقطعة خبز كامل وحبة تمر تعطيك طاقة للتركيز في القسم حتى الظهر."},
    {"audio":"../audio/04_s3.mp3","image":"../img/01_s1.jpg","caption":"نظافة","board_title":"صحة","lines":[{"text":"اغسل يديك قبل الأكل","style":"eq"},{"text":"واغسل أسنانك بعده","style":"label"}],"narration":"النظافة تحميك: اغسل يديك بالماء والصابون قبل الأكل وبعده، واغسل أسنانك مرتين في اليوم لتطرد السوسة. لا تنس غسل الغلال أيضا."},
    {"audio":"../audio/04_s4.mp3","image":"../img/01_s2.jpg","caption":"حركة","board_title":"رياضة","lines":[{"text":"30 دقيقة لعب يوميا","style":"eq"},{"text":"نوم 9 ساعات","style":"op"}],"narration":"الحركة بركة: العب واقفز ثلاثين دقيقة يوميا في الحومة، ونم تسع ساعات ليلا ليكبر جسمك وعقلك. قلل من الشاشات والحلويات."},
    {"audio":"../audio/04_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"أي فطور أصح؟ مقارونة حلوة أم خبز وزيت؟","style":"ask"},{"text":"فكّر","style":"label"},{"text":"خبز وزيت وزيتون","style":"answer"}],"narration":"كويز: أي فطور أصح قبل الامتحان، مقارونة بالسكر أم خبز بزيت الزيتون وحليب؟ فكروا... خبز وزيت وحليب وزيتون تونس أصح وأكثر طاقة. برافو!","pause_after":2},
    {"audio":"../audio/04_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"ارسم طبق فطورك الصحي غدا","style":"ask"},{"text":"وشاركه مع عائلتك","style":"small"}],"narration":"مهمة الدار: ارسم طبق فطورك ليوم الغد واكتب مكوناته. هل هو متوازن؟ شاركه مع أمك وأبيك. أنتم سفراء الصحة، برافو!","confetti":True}
  ]
})

# FRENCH
write_lesson("french","01_sons",{
  "title":"Les sons et les lettres","episode":"1","brand":"3e année · Français","level":"g3","subject":"french","width":1920,"height":1080,"fps":24,
  "yt":{"title":"Les sons et les lettres | Français 3e année 🇫🇷"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"Bonjour les champions !","board_title":"Alphabet","lines":[{"text":"A · B · C · D","style":"eq"},{"text":"Avion · Ballon · Cadeau · Dattes","style":"small"}],"narration":"Bonjour les champions de Bravo Academy ! Aujourd'hui, les sons et les lettres. A comme avion et comme ananas de Gabès, B comme ballon, C comme cadeau, D comme dattes de Tozeur. Répétez avec moi."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s2.jpg","caption":"Je chante l'alphabet","board_title":"Chanson","lines":[{"text":"A B C D E F G","style":"eq"},{"text":"chanter aide à mémoriser","style":"label"}],"narration":"On chante l'alphabet ensemble : A B C D E F G... Chanter aide à mémoriser vite. Chantez trois fois dans la journée."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s1.jpg","caption":"J'écoute le son","board_title":"Son","lines":[{"text":"B = /b/ · P = /p/","style":"eq"},{"text":"oreille et bouche","style":"small"}],"narration":"Chaque lettre a un son. B fait /b/ comme ballon, P fait /p/ comme papillon. Mettez la main sur la gorge, sentez la vibration."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s2.jpg","caption":"J'écris","board_title":"Écrire","lines":[{"text":"A a · B b · C c","style":"eq"},{"text":"majuscule et minuscule","style":"label"}],"narration":"On écrit majuscule et minuscule : A a, B b, C c. Prenez votre cahier et tracez bien les lignes."},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s3.jpg","caption":"Quiz","board_title":"Quiz","lines":[{"text":"B comme ... ? trouve 2 mots","style":"ask"},{"text":"... 3 secondes ...","style":"label"},{"text":"Ballon, Banane, Bravo !","style":"answer"}],"narration":"Quiz : B comme quoi ? Trouvez deux mots qui commencent par B. Réfléchissez trois secondes... Bravo ! Ballon, banane, bonbon, Bravo Academy !","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"Bravo !","board_title":"Défi","lines":[{"text":"Trouve 3 mots avec A","style":"ask"},{"text":"écris-les en commentaire","style":"small"}],"narration":"Défi maison : trouvez trois mots avec la lettre A et écrivez-les en commentaire. Je vous corrige. Bravo les champions !","confetti":True}
  ]
})

write_lesson("french","02_vocab",{
  "title":"Le vocabulaire de la vie quotidienne","episode":"2","brand":"3e année · Français","level":"g3","subject":"french","width":1920,"height":1080,"fps":24,
  "yt":{"title":"Vocabulaire du quotidien | Français 3e"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/01_s2.jpg","caption":"Chez moi à Tunis","board_title":"Maison","lines":[{"text":"table · chaise · porte · fenêtre","style":"eq"}],"narration":"Aujourd'hui, le vocabulaire de la maison à Tunis. Une table, une chaise, une porte, une fenêtre. Touchez chaque objet en le nommant."},
    {"audio":"../audio/02_s2.mp3","image":"../img/01_s1.jpg","caption":"Dans ma chambre","board_title":"Chambre","lines":[{"text":"lit · livre · cartable","style":"eq"},{"text":"mon lit est doux","style":"small"}],"narration":"Dans ma chambre : un lit doux, un livre passionnant, un cartable bleu pour l'école. Mon cartable contient mes livres."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s2.jpg","caption":"Je fais une phrase","board_title":"Phrase","lines":[{"text":"J'ouvre la porte.","style":"eq"},{"text":"Je lis un livre.","style":"small"}],"narration":"Je fais une petite phrase : J'ouvre la porte. Je lis un livre sur mon lit. Sujet, verbe, complément, vous voyez ?"},
    {"audio":"../audio/02_s4.mp3","image":"../img/01_s1.jpg","caption":"Au marché","board_title":"Marché","lines":[{"text":"pain · lait · dattes","style":"eq"}],"narration":"Au marché de Nabeul : du pain, du lait, des dattes. J'achète trois dattes sucrées."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s3.jpg","caption":"Quiz","board_title":"Quiz","lines":[{"text":"Comment dit-on كرّاس en français ?","style":"ask"},{"text":"... réfléchis ...","style":"label"},{"text":"un cahier","style":"answer"}],"narration":"Quiz : comment dit-on كراس en français ? Réfléchissez trois secondes... On dit un cahier ! Et قلم c'est un stylo.","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"Bravo !","board_title":"Défi","lines":[{"text":"Nommez 4 objets de ta chambre","style":"ask"}],"narration":"Défi maison : nommez quatre objets de votre chambre en français et écrivez-les. Je lis tous vos commentaires. Bravo !","confetti":True}
  ]
})

write_lesson("french","03_svc",{
  "title":"Sujet + verbe + complément","episode":"3","brand":"3e année · Français","level":"g3","subject":"french","width":1920,"height":1080,"fps":24,
  "yt":{"title":"Sujet verbe complément | Français 3e"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/01_s2.jpg","caption":"La règle d'or","board_title":"S+V+C","lines":[{"text":"Qui ? + Fait quoi ? + Quoi ?","style":"small"},{"text":"Sujet + Verbe + Complément","style":"eq"}],"narration":"Bonjour ! La phrase simple a trois amis : le sujet qui fait, le verbe qui agit, le complément qui complète. Qui, fait quoi, quoi ?"},
    {"audio":"../audio/03_s2.mp3","image":"../img/01_s2.jpg","caption":"Exemple","board_title":"Exemple","lines":[{"text":"Lina mange une pomme.","style":"eq"},{"text":"S=Lina  V=mange  C=pomme","style":"label"}],"narration":"Exemple délicieux : Lina mange une pomme. Lina est le sujet, mange est le verbe, une pomme est le complément. On ne coupe pas la phrase."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s1.jpg","caption":"En Tunisie","board_title":"Exemple2","lines":[{"text":"Adam lit un livre à Sidi Bou Saïd.","style":"eq"}],"narration":"Autre exemple tunisien : Adam lit un livre à Sidi Bou Saïd. Adam sujet, lit verbe, un livre complément. À Sidi Bou Saïd précise le lieu."},
    {"audio":"../audio/03_s4.mp3","image":"../img/01_s2.jpg","caption":"Attention !","board_title":"Ordre","lines":[{"text":"S+V+C = ordre fixe","style":"eq"},{"text":"Ne mélange pas !","style":"small"}],"narration":"Attention, l'ordre est fixe : sujet, verbe, complément. On ne dit pas mange Lina pomme, on dit Lina mange une pomme. L'ordre, c'est la musique de la phrase."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s3.jpg","caption":"Quiz","board_title":"Quiz","lines":[{"text":"Trouve le sujet: Sami joue au foot.","style":"ask"},{"text":"... 3 sec ...","style":"label"},{"text":"Sami","style":"answer"}],"narration":"Quiz : dans Sami joue au foot, quel est le sujet ? Réfléchissez trois secondes... C'est Sami ! Et le verbe c'est joue. Bravo !","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"Bravo !","board_title":"Défi","lines":[{"text":"Invente une phrase S+V+C","style":"ask"},{"text":"avec ton prénom","style":"small"}],"narration":"Défi maison : inventez une phrase avec sujet verbe complément en utilisant votre prénom. Écrivez-la, je corrige. Bravo les grammairiens !","confetti":True}
  ]
})

write_lesson("french","04_salut",{
  "title":"Les salutations","episode":"4","brand":"3e année · Français","level":"g3","subject":"french","width":1920,"height":1080,"fps":24,
  "yt":{"title":"Les salutations | Français 3e"},
  "scenes":[
    {"audio":"../audio/04_s1.mp3","image":"../img/01_s1.jpg","caption":"Bonjour !","board_title":"Bonjour","lines":[{"text":"Bonjour le matin","style":"eq"},{"text":"Bonsoir le soir · Salut = ami","style":"small"}],"narration":"Bonjour les amis ! Le matin on dit bonjour à la maîtresse, le soir on dit bonsoir à ses parents, et à un copain on dit salut ! Trois mots magiques."},
    {"audio":"../audio/04_s2.mp3","image":"../img/01_s2.jpg","caption":"Politesse","board_title":"Merci","lines":[{"text":"s'il te plaît · merci","style":"eq"},{"text":"pardon · au revoir","style":"small"}],"narration":"La politesse ouvre les portes : s'il te plaît pour demander, merci pour remercier, pardon pour s'excuser, au revoir pour partir."},
    {"audio":"../audio/04_s3.mp3","image":"../img/01_s1.jpg","caption":"Dialogue","board_title":"Dialogue","lines":[{"text":"— Salut Lina! — Salut Adam!","style":"eq"},{"text":"— Comment ça va? — Très bien!","style":"small"}],"narration":"Petit dialogue à Sousse : Salut Lina ! Salut Adam ! Comment ça va ? Très bien merci ! Et toi ? On répète ensemble."},
    {"audio":"../audio/04_s4.mp3","image":"../img/01_s2.jpg","caption":"Sourire","board_title":"Sourire","lines":[{"text":"Un sourire + Bonjour","style":"eq"},{"text":"= journée heureuse","style":"label"}],"narration":"N'oubliez jamais le sourire avec bonjour. Un sourire plus bonjour égale journée heureuse pour tout le monde."},
    {"audio":"../audio/04_s5.mp3","image":"../img/01_s3.jpg","caption":"Quiz","board_title":"Quiz","lines":[{"text":"Que dit-on le soir à maman ?","style":"ask"},{"text":"... réfléchis ...","style":"label"},{"text":"Bonsoir maman !","style":"answer"}],"narration":"Quiz : que dit-on le soir en rentrant à la maison à maman ? Réfléchissez... On dit bonsoir maman ! Et le matin bonjour maman. Bravo !","pause_after":2},
    {"audio":"../audio/04_s6.mp3","image":"../img/01_s3.jpg","caption":"Bravo !","board_title":"Défi","lines":[{"text":"Salue 3 personnes demain en français","style":"ask"}],"narration":"Défi maison : saluez trois personnes demain en français et racontez leur réaction en commentaire. Bravo les polis !","confetti":True}
  ]
})

# CIVIC
write_lesson("civic","01_identity",{
  "title":"الهوية التونسية","episode":"1","brand":"السنة الثالثة أساسي · تربية مدنية","level":"g3","subject":"civic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الهوية التونسية | تربية مدنية الثالثة أساسي 🇹🇳"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"أنا تونسي وأفتخر","board_title":"من أنا؟","lines":[{"text":"أنا تونسي · أتكلّم العربية","style":"eq"},{"text":"وأعيش في تونس الخضراء","style":"small"}],"narration":"مرحبا يا أبطال تونس الخضراء! أنا تونسي، أتكلم العربية وأعيش في بلد جميل من بنزرت إلى برج الخضراء. هويتنا تجمعنا."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s2.jpg","caption":"علمنا","board_title":"الرموز","lines":[{"text":"علم أحمر وهلال ونجمة بيضاء","style":"eq"},{"text":"نشيد: حماة الحمى","style":"small"}],"narration":"رمزنا الأول علم أحمر فيه دائرة بيضاء وهلال ونجمة حمراء. نرفعه في المدرسة ونحترمه. ونشيدنا حماة الحمى نقفه باحترام."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s1.jpg","caption":"عاداتنا","board_title":"هوية","lines":[{"text":"كسكسي · زيتونة · لهجة تونسية","style":"eq"},{"text":"كرم وضيافة","style":"label"}],"narration":"هويتنا أيضا في عاداتنا: كسكسي يوم الجمعة، زيتونة صفاقس، ولهجتنا التونسية الحلوة. والتونسي معروف بالكرم والضيافة."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s2.jpg","caption":"العيش معا","board_title":"قيم","lines":[{"text":"احترام · تعاون · نظام","style":"eq"},{"text":"في القسم والحي","style":"small"}],"narration":"الهوية ليست كلاما فقط، هي سلوك: نحترم بعضنا في القسم، نتعاون في الحي، نحافظ على النظام والنظافة."},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"ما لونا العلم التونسي؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"أحمر وأبيض","style":"answer"}],"narration":"كويز: ما لونا العلم التونسي؟ فكروا ثلاث ثوان... أحمر وأبيض، والهلال والنجمة حمراء. هل تذكرتم؟","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"ارسم العلم واكتب نشيدا صغيرا","style":"ask"}],"narration":"مهمة الدار: ارسم العلم التونسي بدقة واكتب سطرا عن حبك لتونس وشاركه مع عائلتك. أنتم فخر تونس، برافو!","confetti":True}
  ]
})

write_lesson("civic","02_law",{
  "title":"احترام القانون في المدرسة","episode":"2","brand":"السنة الثالثة أساسي · تربية مدنية","level":"g3","subject":"civic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"احترام القانون في المدرسة | مدنية الثالثة"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/01_s2.jpg","caption":"لماذا القانون؟","board_title":"قانون","lines":[{"text":"القانون يحمي الجميع","style":"eq"},{"text":"بلا قانون تعم الفوضى","style":"small"}],"narration":"مرحبا يا منظمين! لماذا نحترم القانون في المدرسة؟ لأن القانون يحمينا جميعا. تخيلوا ممرا بلا قواعد، الكل يدفع والكل يسقط."},
    {"audio":"../audio/02_s2.mp3","image":"../img/01_s3.jpg","caption":"قواعد الصف","board_title":"قواعد","lines":[{"text":"نرفع اليد قبل الكلام","style":"eq"},{"text":"لا ندفع في الممر","style":"label"}],"narration":"قواعد الصف بسيطة: نرفع اليد قبل الكلام، نستمع للمعلم، لا ندفع في الممر، نحافظ على نظافة الطاولة والسبورة."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s1.jpg","caption":"حقوق وواجبات","board_title":"توازن","lines":[{"text":"حقي: أتعلّم بأمان","style":"label"},{"text":"واجبي: أحترم غيري","style":"op"}],"narration":"لنا حقوق وعلينا واجبات. حقنا أن نتعلم بأمان وهدوء، وواجبنا أن نحترم المعلم والرفاق والأدوات. التوازن يصنع مدرسة سعيدة."},
    {"audio":"../audio/02_s4.mp3","image":"../img/01_s2.jpg","caption":"مثال","board_title":"مثال","lines":[{"text":"تأخرت → أعتذر وأدخل بهدوء","style":"eq"}],"narration":"مثال: إذا تأخرت صباحا بسبب الحافلة، أطرق الباب بهدوء وأعتذر وأجلس دون إزعاج. القانون ليس عقابا، بل احترام."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"ماذا تفعل إذا وجدت قلما ضائعا؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"أسلّمه للمعلم","style":"answer"}],"narration":"كويز: وجدت قلما ضائعا في الساحة، ماذا تفعل؟ فكروا ثلاث ثوان... أسلمه للمعلم أو للإدارة، لأن الأمانة من القانون. أحسنتم!","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"اكتب 3 قواعد تحبها في قسمك","style":"ask"}],"narration":"مهمة الدار: اكتب ثلاث قواعد تحبها في قسمك ولماذا تحترمها. شاركها مع أصدقائك. أنتم قدوة النظام، برافو!","confetti":True}
  ]
})

write_lesson("civic","03_coop",{
  "title":"التعاون والعمل الجماعي","episode":"3","brand":"السنة الثالثة أساسي · تربية مدنية","level":"g3","subject":"civic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"التعاون والعمل الجماعي | مدنية الثالثة"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/01_s2.jpg","caption":"معا أقوى","board_title":"تعاون","lines":[{"text":"يد واحدة لا تصفّق","style":"eq"},{"text":"معا ننجز أكثر","style":"label"}],"narration":"مرحبا يا متعاونين! يقول المثل يد واحدة لا تصفق. عندما نتعاون ننجز أكثر وأجمل. مثل خلية النحل في جربة."},
    {"audio":"../audio/03_s2.mp3","image":"../img/01_s1.jpg","caption":"أدوار","board_title":"أدوار","lines":[{"text":"كل واحد له مهمة","style":"eq"},{"text":"قائد · كاتب · رسام","style":"small"}],"narration":"في مشروع القسم، لكل واحد دور: قائد ينظم، كاتب يكتب، رسام يلون. الكل مهم، والنجاح للجميع."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s2.jpg","caption":"نستمع","board_title":"احترام","lines":[{"text":"نستمع لرأي الآخر","style":"eq"},{"text":"نحترم الاختلاف","style":"label"}],"narration":"العمل الجماعي يعني أن نستمع لرأي الآخر حتى لو اختلفنا. نحترم الفكرة ونناقش بهدوء، لا نقاطع."},
    {"audio":"../audio/03_s4.mp3","image":"../img/01_s1.jpg","caption":"مثال","board_title":"مثال","lines":[{"text":"نظافة الساحة معا","style":"eq"},{"text":"10 دقائق والكل نظيف","style":"small"}],"narration":"مثال: تنظيف الساحة معا عشر دقائق والكل نظيف، وحدك ساعة ولا تنتهي. التعاون يربح الوقت."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"متى تعاونت هذا الأسبوع؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"شارك قصتك","style":"answer"}],"narration":"كويز: تذكر متى تعاونت هذا الأسبوع مع زميل أو عائلتك؟ فكروا ثلاث ثوان... شاركوا قصتكم في التعليقات، نحب أن نسمعها.","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"نظّم لعبة جماعية في الحومة","style":"ask"}],"narration":"مهمة الدار: نظموا لعبة جماعية في الحومة ووزعوا الأدوار بالعدل. التقطوا صورة جماعية. أنتم روح الفريق، برافو!","confetti":True}
  ]
})

# ISLAMIC
write_lesson("islamic","01_salat",{
  "title":"الصلاة وأوقاتها","episode":"1","brand":"السنة الثالثة أساسي · تربية إسلامية","level":"g3","subject":"islamic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الصلاة وأوقاتها | تربية إسلامية الثالثة أساسي"},
  "scenes":[
    {"audio":"../audio/01_s1.mp3","image":"../img/01_s1.jpg","caption":"عماد الدين","board_title":"الصلاة","lines":[{"text":"الصلاة صلة مع الله","style":"eq"},{"text":"خمس صلوات في اليوم","style":"label"}],"narration":"السلام عليكم يا أحباب! الصلاة عماد الدين وصلة جميلة مع الله. نفرح بها خمس مرات في اليوم، مثل خمس محطات نور."},
    {"audio":"../audio/01_s2.mp3","image":"../img/01_s2.jpg","caption":"الفجر والظهر","board_title":"الأوقات1","lines":[{"text":"الصبح فجرا · الظهر وسط النهار","style":"eq"},{"text":"العصر بعد الظهر","style":"small"}],"narration":"الصلوات الخمس: الصبح فجرا قبل الشروق، والظهر عندما تكون الشمس في الوسط، والعصر بعد الظهر."},
    {"audio":"../audio/01_s3.mp3","image":"../img/01_s1.jpg","caption":"المغرب والعشاء","board_title":"الأوقات2","lines":[{"text":"المغرب عند الغروب","style":"eq"},{"text":"العشاء ليلا","style":"small"}],"narration":"والمغرب عند غروب الشمس، والعشاء ليلا. لكل صلاة وقتها، والمسلم يحافظ على الوقت مثلما يحافظ على موعده مع أعز حبيب."},
    {"audio":"../audio/01_s4.mp3","image":"../img/01_s2.jpg","caption":"الوضوء","board_title":"طهارة","lines":[{"text":"نتوضأ بماء طاهر","style":"eq"},{"text":"نظافة الجسم والقلب","style":"label"}],"narration":"قبل الصلاة نتوضأ بماء طاهر: نغسل الوجه واليدين ونمسح الرأس ونغسل الرجلين. الوضوء نظافة وطهارة ونشاط."},
    {"audio":"../audio/01_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"كم صلاة في اليوم؟ سمّها","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"5: صبح ظهر عصر مغرب عشاء","style":"answer"}],"narration":"كويز: كم صلاة في اليوم وسمّها بالترتيب؟ فكروا ثلاث ثوان... خمس صلوات: الصبح والظهر والعصر والمغرب والعشاء. هل حفظتموها؟","pause_after":2},
    {"audio":"../audio/01_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"احفظ أوقات الصلوات","style":"ask"},{"text":"وصلّ مع عائلتك","style":"small"}],"narration":"مهمة الدار: احفظوا أوقات الصلوات الخمس وصلّوا مع عائلتكم جماعة. الصلاة نور وبركة. برافو يا صالحين!","confetti":True}
  ]
})

write_lesson("islamic","02_sidq",{
  "title":"الصدق والأمانة","episode":"2","brand":"السنة الثالثة أساسي · تربية إسلامية","level":"g3","subject":"islamic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"الصدق والأمانة | تربية إسلامية الثالثة"},
  "scenes":[
    {"audio":"../audio/02_s1.mp3","image":"../img/01_s1.jpg","caption":"خلق النبي","board_title":"صدق","lines":[{"text":"الصدق يهدي إلى الجنة","style":"eq"},{"text":"الكذب يهدي إلى النار","style":"small"}],"narration":"أهلا يا صادقين! نبينا محمد صلى الله عليه وسلم كان يلقب بالصادق الأمين قبل البعثة. الصدق يهدي إلى الجنة والكذب يهدي إلى النار."},
    {"audio":"../audio/02_s2.mp3","image":"../img/01_s2.jpg","caption":"في المدرسة","board_title":"مثال","lines":[{"text":"كسرت القلم → أقول الحقيقة","style":"eq"},{"text":"وأعتذر","style":"label"}],"narration":"مثال في القسم: إذا كسرت قلما بالخطأ، قل الحقيقة واعتذر. المعلم يحب الصادق ويعفو عنه، والكاذب يفقد ثقة الناس."},
    {"audio":"../audio/02_s3.mp3","image":"../img/01_s1.jpg","caption":"الأمانة","board_title":"أمانة","lines":[{"text":"أمانة القلم والكتاب","style":"eq"},{"text":"وأمانة السر","style":"small"}],"narration":"الأمانة أخت الصدق: إذا استعرت قلما فحافظ عليه ورده، وإذا ائتمنك صديق على سر فاحفظه. الأمانة تجعل الناس يحبونك."},
    {"audio":"../audio/02_s4.mp3","image":"../img/01_s2.jpg","caption":"قصة","board_title":"قصة","lines":[{"text":"راعي غنم صادق","style":"eq"},{"text":"لم يكذب ونجا","style":"label"}],"narration":"قصة قصيرة: راعٍ سأله ذئب كاذب أين الغنم فقال لا أكذب، فجاء أهل القرية وأنقذوه. الصدق نجاة."},
    {"audio":"../audio/02_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"ماذا تفعل إذا وجدت محفظة؟","style":"ask"},{"text":"فكّر 3 ثوان","style":"label"},{"text":"أردّها لصاحبها","style":"answer"}],"narration":"كويز: وجدت محفظة في الساحة فيها نقود، ماذا تفعل؟ فكروا ثلاث ثوان... أردها لصاحبها أو أسلمها للمعلم، هذه الأمانة. أحسنتم!","pause_after":2},
    {"audio":"../audio/02_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"كن صادقا اليوم كله","style":"ask"},{"text":"واحك لعائلتك","style":"small"}],"narration":"مهمة الدار: كونوا صادقين اليوم كله ولو كان الصدق صعبا، واحكوا لعائلتكم ما فعلتم. الصدق نور، برافو!","confetti":True}
  ]
})

write_lesson("islamic","03_nuh",{
  "title":"قصص الأنبياء: نوح","episode":"3","brand":"السنة الثالثة أساسي · تربية إسلامية","level":"g3","subject":"islamic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"قصة نوح عليه السلام | تربية إسلامية الثالثة"},
  "scenes":[
    {"audio":"../audio/03_s1.mp3","image":"../img/01_s1.jpg","caption":"نبي صبور","board_title":"نوح","lines":[{"text":"نوح يدعو قومه 950 سنة","style":"eq"},{"text":"صبر عجيب!","style":"label"}],"narration":"السلام عليكم! اليوم قصة نبي صبور جدا هو نوح عليه السلام. دعا قومه تسعمائة وخمسين سنة ليعبدوا الله وحده، لكن أكثرهم لم يستمع."},
    {"audio":"../audio/03_s2.mp3","image":"../img/01_s2.jpg","caption":"السفينة","board_title":"سفينة","lines":[{"text":"أمره الله ببناء سفينة كبيرة","style":"eq"},{"text":"في الصحراء!","style":"small"}],"narration":"أمره الله أن يبني سفينة كبيرة في الصحراء، فضحك منه قومه. لكن نوحا أطاع ربه وجمع المؤمنين والحيوانات زوجين زوجين."},
    {"audio":"../audio/03_s3.mp3","image":"../img/01_s1.jpg","caption":"الطوفان","board_title":"طوفان","lines":[{"text":"جاء الماء من كل مكان","style":"eq"},{"text":"ونجا المؤمنون","style":"answer"}],"narration":"جاء الطوفان، ماء من السماء وماء من الأرض، وغرق الكافرون ونجا المؤمنون في السفينة. وعد الله حق."},
    {"audio":"../audio/03_s4.mp3","image":"../img/01_s2.jpg","caption":"حمامة وغصن","board_title":"نهاية","lines":[{"text":"أرسل حمامة فعادت بغصن","style":"eq"},{"text":"انتهى الطوفان","style":"small"}],"narration":"بعد أيام أرسل نوح حمامة فعادت بغصن زيتون، علامة أن الأرض جفت. شكر نوح ربه وسجد."},
    {"audio":"../audio/03_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"كم سنة دعا نوح قومه؟","style":"ask"},{"text":"فكّر","style":"label"},{"text":"950 سنة","style":"answer"}],"narration":"كويز: كم سنة دعا نوح قومه؟ فكروا... تسعمائة وخمسون سنة وهو صابر لا يمل. هل تتحملون؟","pause_after":2},
    {"audio":"../audio/03_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"عبرة","lines":[{"text":"العبرة: الصبر وطاعة الله","style":"eq"},{"text":"احك القصة لعائلتك","style":"small"}],"narration":"العبرة من قصة نوح: الصبر وطاعة الله تنجيان. احكوا القصة لعائلتكم بأسلوبكم وارسموا السفينة. برافو يا صغار!","confetti":True}
  ]
})

write_lesson("islamic","04_masjid",{
  "title":"آداب المسجد","episode":"4","brand":"السنة الثالثة أساسي · تربية إسلامية","level":"g3","subject":"islamic","width":1920,"height":1080,"fps":24,
  "yt":{"title":"آداب المسجد | تربية إسلامية الثالثة"},
  "scenes":[
    {"audio":"../audio/04_s1.mp3","image":"../img/01_s1.jpg","caption":"بيت الله","board_title":"مسجد","lines":[{"text":"المسجد بيت الله","style":"eq"},{"text":"نظيف وهادئ","style":"label"}],"narration":"مرحبا يا زوار بيت الله! المسجد مكان نظيف وهادئ نصلي فيه ونذكر الله. بيت الله أحب مكان."},
    {"audio":"../audio/04_s2.mp3","image":"../img/01_s2.jpg","caption":"قبل الدخول","board_title":"آداب1","lines":[{"text":"نتوضأ · نلبس نظيفا","style":"eq"},{"text":"ندخل باليمنى ونقول الدعاء","style":"small"}],"narration":"قبل الدخول نتوضأ ونلبس ثيابا نظيفة وندخل بالرجل اليمنى ونقول دعاء دخول المسجد: اللهم افتح لي أبواب رحمتك."},
    {"audio":"../audio/04_s3.mp3","image":"../img/01_s1.jpg","caption":"داخل المسجد","board_title":"آداب2","lines":[{"text":"نصلي تحية المسجد","style":"eq"},{"text":"لا نرفع صوتنا","style":"label"}],"narration":"داخل المسجد نصلي ركعتي تحية المسجد ونجلس بهدوء ولا نرفع صوتنا ولا نركض. نحترم المصلين."},
    {"audio":"../audio/04_s4.mp3","image":"../img/01_s2.jpg","caption":"الخروج","board_title":"خروج","lines":[{"text":"نخرج باليسرى","style":"eq"},{"text":"دعاء: اللهم إني أسألك من فضلك","style":"small"}],"narration":"عند الخروج نخرج بالرجل اليسرى ونقول اللهم إني أسألك من فضلك. ونسلم على الناس بابتسامة."},
    {"audio":"../audio/04_s5.mp3","image":"../img/01_s3.jpg","caption":"كويز","board_title":"كويز","lines":[{"text":"بأي رجل ندخل المسجد؟","style":"ask"},{"text":"فكّر","style":"label"},{"text":"باليمنى","style":"answer"}],"narration":"كويز: بأي رجل ندخل المسجد؟ فكروا... بالرجل اليمنى، ونخرج باليسرى. تذكروا!","pause_after":2},
    {"audio":"../audio/04_s6.mp3","image":"../img/01_s3.jpg","caption":"برافو!","board_title":"مهمة","lines":[{"text":"اذهب للمسجد مع وليك","style":"ask"},{"text":"وطبّق الآداب","style":"small"}],"narration":"مهمة الدار: اذهبوا للمسجد مع وليكم يوم الجمعة وطبقوا آداب المسجد التي تعلمناها. أنتم مؤدبون، برافو!","confetti":True}
  ]
})

print("All lessons expanded")
