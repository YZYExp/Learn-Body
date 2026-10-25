"""Original conceptual connection diagram; not an anatomical-scale rendering."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import math,json
R=Path(__file__).resolve().parents[1]
F='/usr/local/share/fonts/motion/NotoSansCJKsc-Bold.otf'
def font(n):return ImageFont.truetype(F,n)
im=Image.new('RGB',(1700,1100),'#faf8f3');d=ImageDraw.Draw(im)
ink='#203344';blue='#2377aa';red='#bc5147';purple='#795583'
def text(x,y,s,n=30,col=ink):d.text((x,y),s,font=font(n),fill=col)
def line(points,col,w=12):d.line(points,fill=col,width=w,joint='curve')
def arrow(a,b,col,w=8):
 d.line([a,b],fill=col,width=w);ang=math.atan2(b[1]-a[1],b[0]-a[0]);pts=[b,(b[0]-26*math.cos(ang-.5),b[1]-26*math.sin(ang-.5)),(b[0]-26*math.cos(ang+.5),b[1]-26*math.sin(ang+.5))];d.polygon(pts,fill=col)
text(70,60,'从神经根到脊神经分支',54)
text(70,140,'感觉传入与运动传出分走前、后根；汇合后由混合神经承载',30)
d.rounded_rectangle((70,270,310,850),radius=28,fill='#e0e5e6',outline=ink,width=3)
text(125,505,'脊髓',44)
line([(310,390),(670,390),(870,560)],blue)
line([(310,735),(670,735),(870,560)],red)
d.ellipse((450,350,590,430),fill='#c9e3ef',outline=blue,width=5)
text(370,265,'后根：感觉传入',32,blue)
text(425,455,'后根神经节',30,blue)
arrow((425,390),(330,390),blue)
text(375,790,'前根：运动传出',32,red)
arrow((335,735),(430,735),red)
line([(870,560),(1120,560)],purple,20)
text(870,475,'脊神经',34,purple)
text(865,625,'含感觉及运动纤维',27,purple)
line([(1120,560),(1430,355)],purple,16);line([(1120,560),(1430,770)],purple,16)
text(1280,270,'后支',34,purple);text(1260,815,'前支',34,purple)
text(1370,420,'均为混合支',27,purple)
text(1370,705,'均为混合支',27,purple)
text(70,950,'连接关系示意，不按解剖比例；“后支”不同于“后根”。',30)
text(70,1000,'原创读图辅助 · 依据 OpenStax A&P 2e §13.2、§13.4',25)
fs=json.loads((R/'references/figures.json').read_text())
f=next(x for x in fs if x['original_number']=='原创辅助图')
p=R/f['path']; im.save(p)
# Original typographic cover. Nested shapes are abstract and do not depict anatomical layers.
im=Image.new('RGB',(1400,2100),'#f3eee3');d=ImageDraw.Draw(im)
d.rectangle((0,0,50,2100),fill='#204957')
d.text((135,150),'AN ATLAS OF THE HUMAN BODY',font=font(32),fill='#52727b')
d.text((125,315),'人体',font=font(185),fill='#163a48')
d.text((135,555),'从外到内',font=font(116),fill='#163a48')
d.text((140,760),'层次 · 空间 · 连接 · 功能',font=font(39),fill='#52727b')
colors=['#d9b99b','#c77d70','#b75e55','#d8c9ac','#8eaaaa','#356575']
for i,c in enumerate(colors):
 x=180+i*90;y=970+i*75
 d.rounded_rectangle((x,y,1200-i*40,1810-i*30),radius=80,fill=c)
d.text((140,1920),'图解知识读本   /   2026',font=font(36),fill='#52727b')
im.save(R/'assets/cover.png')
