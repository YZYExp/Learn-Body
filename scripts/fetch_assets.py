"""Restore missing source images from curated provenance. Existing assets are kept."""
from pathlib import Path
from urllib.request import urlopen,Request
import json
from PIL import Image,ImageFile
R=Path(__file__).resolve().parents[1]
for f in json.loads((R/'references/figures.json').read_text()):
 p=R/f['path']
 if p.exists():continue
 if not f['original_url']:raise RuntimeError('Original diagram missing; restore it from Git or source package: '+f['path'])
 data=urlopen(Request(f['original_url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 try:Image.open(p).load()
 except OSError:
  ImageFile.LOAD_TRUNCATED_IMAGES=True;im=Image.open(p);im.load();im=im.convert('RGB');im.save(p,format='JPEG',quality=96);ImageFile.LOAD_TRUNCATED_IMAGES=False
 print(f['path'])
