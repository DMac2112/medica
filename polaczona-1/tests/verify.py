from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json,hashlib
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.sources=[];self.h1=0;self.robots=False;self.lang=False;self.forms=[];self.details=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='html':self.lang=a.get('lang')=='pl'
  if tag=='h1':self.h1+=1
  if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content')=='noindex, nofollow'
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag in ['script','img'] and a.get('src'):self.sources.append(a['src'])
  if tag=='link' and a.get('href'):self.sources.append(a['href'])
  if tag in ['form','input','textarea']:self.forms.append(tag)
  if tag=='details':self.details+=1
pages={}
for f in root.glob('*.html'):
 p=Page();p.feed(f.read_text());pages[f.name]=p
 assert p.lang and p.robots and p.h1==1,(f.name,'lang/noindex/h1')
 assert len(p.ids)==len(set(p.ids)),(f.name,'duplicate id')
 assert not p.forms,(f.name,'patient data form')
 assert p.links[0]=='#tresc',(f.name,'skip link')
for name,p in pages.items():
 for href in p.links+p.sources:
  url=urlsplit(href)
  if url.scheme or url.netloc:
   if href in p.sources:raise AssertionError(('external resource',href))
   continue
  path=(root/unquote(url.path)).resolve() if url.path else root/name
  assert path.exists(),(name,href,'broken path')
  if url.fragment and path.suffix=='.html':
   assert url.fragment in pages[path.name].ids,(name,href,'broken anchor')
 for href in p.links:
  if href.startswith('tel:'):assert re.fullmatch(r'tel:\+48\d{9}',href),(name,href)
fonts=re.findall(r"url\('([^']+)'\)",(root/'styles.css').read_text())
assert all((root/f).exists() for f in fonts)
assert len(pages)==6
assert pages['index.html'].details==6,'No-JS weekly fallback missing'
assert pages['kontakt.html'].details==2,'Both original notices must remain'
manifest=json.loads((root.parent/'hub/image-sources.json').read_text())
photo=root.parent/'centrum/assets/reception-Brh0pYck.jpg'
assert hashlib.sha256(photo.read_bytes()).hexdigest() in [p['sha256'] for p in manifest['images']]
def lum(col):
 vals=[int(col[i:i+2],16)/255 for i in (1,3,5)]
 vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
 return sum(a*b for a,b in zip(vals,[.2126,.7152,.0722]))
for fg,bg in [('#b3141f','#ffffff'),('#385e4a','#edf3ef'),('#526259','#ffffff'),('#526259','#edf3ef'),('#242c29','#ffffff')]:
 a,b=sorted([lum(fg),lum(bg)])
 ratio=(b+.05)/(a+.05)
 assert ratio>=4.5,(fg,bg,ratio)
 print(f'Contrast {fg}/{bg}: {ratio:.2f}:1')
print('PASS: 6 pages; local links/anchors/fonts/images; noindex; Polish; one H1; no forms/external resources; no-JS fallback; both notices; verified original photo.')
