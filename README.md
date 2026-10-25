# 人体，从外到内

一部沿着层次、空间与连接阅读身体的中文图解入门书。面向非专业兴趣读者，从体表到组织、运动结构、胸腹盆器官，再进入神经感觉、内分泌与细胞。

本版24章，58幅正文教学图（57幅OpenStax教材图与1幅原创中文连接图），另有导读、术语与路线自检、影像阅读及资料附录。保留原图英文标签，逐图附中文术语对应与观察顺序。

## 阅读顺序

[导读](appendices/00-preface.md)

- [1. 先会定位：体表、方向与切面](chapters/01-orientation.md)
- [2. 放大一层：组织如何组成身体](chapters/02-tissues.md)
- [3. 皮肤：屏障、感觉与散热](chapters/03-skin.md)
- [4. 皮下脂肪与筋膜：形体之间的连接](chapters/04-fascia.md)
- [5. 肌肉：从轮廓走向收缩](chapters/05-muscle.md)
- [6. 骨骼：有生命的支架](chapters/06-skeleton.md)
- [7. 关节：稳定与活动的交换](chapters/07-joints.md)
- [8. 头面部：颅骨、表情与咀嚼](chapters/08-head.md)
- [9. 颈背与脊柱：支撑、通道和姿势](chapters/09-spine.md)
- [10. 肩到手：把力量送到指尖](chapters/10-upper-limb.md)
- [11. 髋到足：承重、步行与足弓](chapters/11-lower-limb.md)
- [12. 打开胸廓：肺、胸膜与呼吸](chapters/12-thorax.md)
- [13. 心脏：四个腔室与两条循环](chapters/13-heart.md)
- [14. 血管与淋巴：遍布层间的运输网](chapters/14-vessels.md)
- [15. 走进腹部：腹壁、腹膜与器官位置](chapters/15-abdomen.md)
- [16. 消化管与肝胰：食物在体内的旅程](chapters/16-digestion.md)
- [17. 肾与泌尿道：过滤、回收和排出](chapters/17-urinary.md)
- [18. 盆腔与生殖：同一空间的不同安排](chapters/18-pelvis.md)
- [19. 脑与脊髓：骨性保护中的中枢](chapters/19-brain.md)
- [20. 周围神经：感觉、运动与自主调节](chapters/20-nerves.md)
- [21. 眼耳鼻舌：感觉器官怎样接入神经](chapters/21-senses.md)
- [22. 内分泌：分散在身体里的化学信号站](chapters/22-endocrine.md)
- [23. 从器官走到细胞：结构如何跨越尺度](chapters/23-microstructure.md)
- [24. 把身体重新连起来：动作、呼吸与稳态](chapters/24-integration.md)

[易混术语与路线自检](appendices/25-glossary.md) · [图像与医学影像](appendices/26-imaging.md) · [资料与图像说明](appendices/27-sources.md)

## 构建与验证

依赖：Python 3.10+、Pillow、Pandoc 3.x。内容和图片已经随工程提供，普通构建不需下载外部资源。

```bash
python -m pip install Pillow
python scripts/check.py
python scripts/build.py
python scripts/check.py
```

阅读包输出至 `build/Human-Body-Outside-In.epub`，合并主稿输出至 `build/Human-Body-Outside-In.md`。EPUB保持图片纵横比，供移动端逐章阅读；原图在 `assets/images/`，阅读包会另生成尺寸适合阅读器的图像副本，不改动原图。

`book.json` 是章节顺序、标题和资源路径的单一清单，后续主页可直接消费它与分章Markdown。网站由轻量 CI 从同一份清单与分章内容构建。

## 编辑文件

- `references/figures.json`：逐图来源、原始图注、许可、中文读图说明及处理记录。
- `editorial/image-index.md`：内部图片审查索引，不编入阅读版。
- `editorial/review.md`：交叉审校与图片删改记录。
- `scripts/fetch_assets.py`：按已核验的来源补回缺失的外部原图；通常不需运行。原创图和封面以工程及Git中的文件为准。
- `scripts/draw_guides.py`：重绘原创神经连接示意与抽象封面；需本机提供Noto Sans CJK中文字体，路径可按环境修改。

## 许可

本书按 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 提供。图源和显微照片署名就近保留，图像为教材示意与组织样本，不将其视为每位个体的精确模板。未使用OpenStax商标图案或教材封面。

## 网页阅读与发布

GitHub Pages 的 Source 设为 GitHub Actions 后，推送 main 自动构建并发布。PR 仅构建与检查，不部署。

```bash
python -m pip install Markdown==3.7
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

构建检查所有站内链接和配图路径。输出在 `_site/`，不执行 EPUB、PDF、图像生成或外部素材下载。目录、逐章导航、附录和原有来源署名从现有稿件生成。
