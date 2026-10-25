from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=[
('orientation','先会定位：体表、方向与切面',['1-6-anatomical-terminology']),
('tissues','放大一层：组织如何组成身体',['4-1-types-of-tissues','4-3-connective-tissue-supports-and-protects']),
('skin','皮肤：屏障、感觉与散热',['5-1-layers-of-the-skin','5-2-accessory-structures-of-the-skin']),
('fascia','皮下脂肪与筋膜：形体之间的连接',['4-3-connective-tissue-supports-and-protects']),
('muscle','肌肉：从轮廓走向收缩',['10-2-skeletal-muscle','10-3-muscle-fiber-contraction-and-relaxation']),
('skeleton','骨骼：有生命的支架',['6-3-bone-structure','7-1-divisions-of-the-skeletal-system']),
('joints','关节：稳定与活动的交换',['9-4-synovial-joints','9-5-types-of-body-movements']),
('head','头面部：颅骨、表情与咀嚼',['7-2-the-skull','11-3-axial-muscles-of-the-head-neck-and-back']),
('spine','颈背与脊柱：支撑、通道和姿势',['7-3-the-vertebral-column','11-4-axial-muscles-of-the-abdominal-wall-and-thorax']),
('upper-limb','肩到手：把力量送到指尖',['8-1-the-pectoral-girdle','8-2-bones-of-the-upper-limb','11-5-muscles-of-the-pectoral-girdle-and-upper-limbs']),
('lower-limb','髋到足：承重、步行与足弓',['8-4-bones-of-the-lower-limb','11-6-appendicular-muscles-of-the-pelvic-girdle-and-lower-limbs']),
('thorax','打开胸廓：肺、胸膜与呼吸',['22-1-organs-and-structures-of-the-respiratory-system','22-2-the-lungs']),
('heart','心脏：四个腔室与两条循环',['19-1-heart-anatomy','19-4-cardiac-physiology']),
('vessels','血管与淋巴：遍布层间的运输网',['20-1-structure-and-function-of-blood-vessels','21-1-anatomy-of-the-lymphatic-and-immune-systems']),
('abdomen','走进腹部：腹壁、腹膜与器官位置',['23-1-overview-of-the-digestive-system','23-5-the-small-and-large-intestines']),
('digestion','消化管与肝胰：食物在体内的旅程',['23-4-the-stomach','23-6-accessory-organs-in-digestion-the-liver-pancreas-and-gallbladder']),
('urinary','肾与泌尿道：过滤、回收和排出',['25-3-gross-anatomy-of-the-kidney','25-4-microscopic-anatomy-of-the-kidney']),
('pelvis','盆腔与生殖：同一空间的不同安排',['27-1-anatomy-and-physiology-of-the-male-reproductive-system','27-2-anatomy-and-physiology-of-the-female-reproductive-system']),
('brain','脑与脊髓：骨性保护中的中枢',['13-2-the-central-nervous-system','13-3-circulation-and-the-central-nervous-system']),
('nerves','周围神经：感觉、运动与自主调节',['13-4-the-peripheral-nervous-system','15-1-divisions-of-the-autonomic-nervous-system']),
('senses','眼耳鼻舌：感觉器官怎样接入神经',['14-1-sensory-perception']),
('endocrine','内分泌：分散在身体里的化学信号站',['17-1-an-overview-of-the-endocrine-system','17-3-the-pituitary-gland-and-hypothalamus']),
('microstructure','从器官走到细胞：结构如何跨越尺度',['3-2-the-cytoplasm-and-cellular-organelles','4-2-epithelial-tissue']),
('integration','把身体重新连起来：动作、呼吸与稳态',['1-5-homeostasis'])]
chapters=[]
for i,(slug,title,sources) in enumerate(data,1):
 chapters.append(dict(id=f'{i:02}',slug=slug,title=title,source=f'chapters/{i:02}-{slug}.md',sections=sources))
(root/'book.json').write_text(json.dumps(dict(title='人体，从外到内',subtitle='一部沿着层次、空间与连接阅读身体的图解入门书',language='zh-CN',chapters=chapters),ensure_ascii=False,indent=2))
(root/'editorial/plan.md').write_text('''# 编辑约定与覆盖计划\n\n读者为兴趣学习的非专业成人。正文客观讲结构与功能，不以生图、健美或绘画技法为主线。正常人体为主，区分变异，不提供诊断治疗和危险的自我触压练习。\n\n阅读顺序：定位与组织→体表与浅层→运动支架→局部解剖→胸腹盆器官→神经感觉与内分泌→微观与整合。层次是观察路线，不是所有部位统一的套娃。男性与女性解剖均覆盖；年龄、体型和个体变异在正文解释。\n\n图源以 OpenStax 教材插图为主，保留原图英文标注，正文逐图给中文对应和观察顺序；不伪装为中文原图。原图署名、许可和源页逐一入索引。配图按关系选择，不固定六格或六类。\n\n分工：A 01–06、B 07–12、C 13–18、D 19–24；主编负责来源、下载、插图整合、全书审校、构建、Git 和交付。\n\n书名、章节顺序和路径以 book.json 为准。所有计划章节均须完成正文；不以大纲和样章充当成书。\n''')
(root/'.gitignore').write_text('build/\n__pycache__/\n')
