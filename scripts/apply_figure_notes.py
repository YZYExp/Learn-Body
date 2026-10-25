"""Synchronize reviewed bilingual labels and spatial reading notes into each figure."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
def cell(value):return value.replace('|',r'\|').replace('\n',' ')
def main():
 book=json.loads((R/'book.json').read_text());figures=json.loads((R/'references/figures.json').read_text());notes={}
 for p in sorted((R/'editorial/localization').glob('zh-*.json')):
  d=json.loads(p.read_text());assert not set(d)&set(notes),p;notes.update(d)
 assert set(notes)=={f['id'] for f in figures},'Localization must cover all figures'
 for f in figures:
  data=notes[f['id']];assert len(data['reading_zh'])>=3,f['id'];assert len(data['labels'])>=1 or f['original_number']=='原创辅助图',f['id']
  f['reading_zh_full']=data['reading_zh'];f['labels_zh_full']=data['labels']
  f['guide_zh']=' '.join(data['reading_zh']);f['labels_zh']='；'.join(x['en']+' '+x['zh'] for x in data['labels'])
  p=R/next(c['source'] for c in book['chapters'] if c['id']==f['chapter']);s=p.read_text();pattern=r'^### 图 '+re.escape(f['id'])+r'｜.*?(?=^#{2,3} |\Z)';m=re.search(pattern,s,re.M|re.S);assert m,f['id'];old=m.group()
  title=old.splitlines()[0];image=re.search(r'!\[[^\]]*\]\([^\n]+\)',old).group()
  footer=old[old.index('*来源：'):].strip()
  # Keep original sample-species notes beside the corresponding image.
  sample=''
  if '**原图样本说明：**' in old:
   sample=re.search(r'\*\*原图样本说明：\*\*[^\n]+',old).group()+'\n\n'
  new=title+'\n\n'+image+'\n\n#### 中文读图说明\n\n'+'\n\n'.join(data['reading_zh'])+'\n\n'+sample
  if data['labels']:
   new+='#### 图中英文标注逐项对照\n\n| 图中英文 | 中文名称 | 在图中怎样理解 |\n| --- | --- | --- |\n'
   for label in data['labels']:
    assert label['en'] and label['zh'] and label['note'],f['id'];new+='| '+' | '.join(cell(label[k]) for k in ('en','zh','note'))+' |\n'
   new+='\n'
  new+=footer+'\n\n';p.write_text(s[:m.start()]+new+s[m.end():])
 (R/'references/figures.json').write_text(json.dumps(figures,ensure_ascii=False,indent=2))
 print(json.dumps({'figures':len(figures),'bilingual_entries':sum(len(x['labels']) for x in notes.values())},ensure_ascii=False))
if __name__=='__main__':main()
