"""Build a portable, reflowable EPUB from the single Markdown source tree."""
from pathlib import Path
import json,re,subprocess
from PIL import Image
R=Path(__file__).resolve().parents[1]
def main():
 b=json.loads((R/'book.json').read_text()); out=R/'build';out.mkdir(exist_ok=True);imgdir=out/'epub-images';imgdir.mkdir(exist_ok=True)
 fs=json.loads((R/'references/figures.json').read_text()); replacements={}
 for f in fs:
  im=Image.open(R/f['path']).convert('RGB');im.thumbnail((1800,2400))
  p=imgdir/(f['id']+'.jpg');im.save(p,quality=90,optimize=True)
  replacements['../'+f['path']]=p.relative_to(R).as_posix()
 files=b['frontmatter']+[c['source'] for c in b['chapters']]+b['backmatter']
 combined=[]
 for name in files:
  s=(R/name).read_text()
  for src,dest in replacements.items():s=s.replace(src,dest)
  combined.append(s)
 (out/'epub.md').write_text('\n\n'.join(combined))
 metadata={'title':b['title'],'subtitle':b['subtitle'],'lang':'zh-CN','date':b['edition'],'rights':'CC BY-NC-SA 4.0; source image attributions accompany figures','toc-title':'目录','identifier':'urn:human-body-atlas:2026-10-25'}
 (out/'metadata.json').write_text(json.dumps(metadata,ensure_ascii=False))
 subprocess.run(['pandoc','build/epub.md','-o','build/Human-Body-Outside-In.epub','--from=markdown','--to=epub3','--toc','--toc-depth=1','--split-level=1','--metadata-file=build/metadata.json','--epub-cover-image=assets/cover.png','--css=scripts/epub.css'],cwd=R,check=True)
 # Also produce a merged Markdown for editors, preserving image paths from root.
 full='\n\n'.join((R/n).read_text().replace('../assets/','assets/') for n in files)
 (out/'Human-Body-Outside-In.md').write_text(full)
 print(out/'Human-Body-Outside-In.epub')
if __name__=='__main__':main()
