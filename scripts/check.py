"""Validate source paths, image decoding, source coverage and packaged EPUB links."""
from pathlib import Path,PurePosixPath
import json,re,zipfile,xml.etree.ElementTree as ET,posixpath
from PIL import Image
R=Path(__file__).resolve().parents[1]
def main():
 b=json.loads((R/'book.json').read_text());fs=json.loads((R/'references/figures.json').read_text());alltext='';han=0
 assert len({c['id'] for c in b['chapters']})==len(b['chapters'])
 for c in b['chapters']:
  p=R/c['source'];s=p.read_text();alltext+=s;han+=len(re.findall('[\u4e00-\u9fff]',s));assert len(re.findall('[\u4e00-\u9fff]',s))>1400,c['id']
  assert 'https://' in s and '![' in s,c['id']
  assert not re.search(r'\bTODO\b|待配图|插图占位',s),c['id']
  for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s):assert (p.parent/image).exists(),image
 for f in fs:
  Image.open(R/f['path']).load();assert f"图 {f['id']}｜" in alltext,f['id']
  assert f['attribution'] and f['license']
  assert len(f.get('reading_zh_full',[]))>=3,('Missing Chinese reading guide',f['id'])
  assert len(f.get('labels_zh_full',[]))>=1 or f['original_number']=='原创辅助图',('Missing label translations',f['id'])
 assert len(re.findall(r'!\[',alltext))==len(fs)
 ep=R/'build/Human-Body-Outside-In.epub'
 if ep.exists():
  with zipfile.ZipFile(ep) as z:
   names=set(z.namelist());assert z.read('mimetype')==b'application/epub+zip';images=0
   for name in names:
    if name.endswith(('.xhtml','.opf','.ncx','.xml')):
     rt=ET.fromstring(z.read(name))
     for node in rt.iter():
      for attr in ('src','href'):
       target=node.attrib.get(attr,'')
       if not target or target.startswith(('http:','https:','mailto:','data:','#')):continue
       target=target.split('#')[0]
       resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),target));assert resolved in names,(name,target)
      if node.tag.endswith('}img'):images+=1
   assert images==len(fs),(images,len(fs))
   assert any('cover' in n and n.endswith(('.png','.jpg')) for n in names)
 print(json.dumps({'chapters':len(b['chapters']),'body_figures':len(fs),'body_han_characters_including_captions':han,'epub_checked':ep.exists()},ensure_ascii=False))
if __name__=='__main__':main()
