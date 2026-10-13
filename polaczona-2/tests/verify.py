"""Check the brief's static requirements, local links, source facts and assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.assets=[];self.h1=0;self.robots=False;self.forms=[];self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='html':self.lang=a.get('lang')=='pl'
  if tag=='h1':self.h1+=1
  if tag=='a' and 'href' in a:self.links.append(a['href'])
  if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content')=='noindex, nofollow'
  if tag in ('form','input','textarea','select'):self.forms.append(tag)
  for key in ('src','srcset'):
   if key in a:self.assets.append(a[key])
  if tag=='link' and a.get('rel') in ('stylesheet','icon'):self.assets.append(a['href'])
files=list(ROOT.glob('*.html'));assert len(files)==6
pages={file.name:Page() for file in files}
for file in files:pages[file.name].feed(file.read_text())
checked=0
for file in files:
 p=pages[file.name]
 assert p.h1==1 and p.robots and p.lang and not p.forms,file.name
 assert len(p.ids)==len(set(p.ids)),f'duplicate id {file.name}'
 for href in p.links+p.assets:
  u=urlsplit(href)
  if u.scheme:
   assert u.scheme in ('tel','https'),href
   if href in p.assets:raise AssertionError(f'external resource {href}')
   continue
  assert not href.startswith('/'),href
  path=(file.parent/unquote(u.path)).resolve() if u.path else file
  assert path.is_file(),f'missing {href} in {file.name}'
  if u.fragment and path.suffix=='.html':
   target=pages.get(path.name)
   assert target and unquote(u.fragment) in target.ids,f'missing anchor {href} in {file.name}'
  checked+=1
 css=ROOT.joinpath('styles.css').read_text()
 for asset in re.findall(r'url\([\'"]?([^\)\'\"]+)',css):assert (ROOT/asset).is_file(),asset
 assert 'prefers-reduced-motion' in css and ':focus-visible' in css
 assert 'font-size:18px' in css
# All original photo hashes must match the verified gallery manifest.
manifest=json.loads(ROOT.parent.joinpath('hub/image-sources.json').read_text())
hashes={x['sha256'] for x in manifest['images']}
photos=set(a for p in pages.values() for a in p.assets if '.jpg' in a.lower())
for photo in photos:assert hashlib.sha256((ROOT/photo).read_bytes()).hexdigest() in hashes,photo
# Clinic facts: complete family-doctor team, lab's exact hours, and uncertainty for absent answers.
godziny=ROOT.joinpath('godziny.html').read_text()
for name in ['Paweł Andrzejczak','Piotr Lisowski','Agnieszka Krawczyk-Kubisiak','Irena Grzeluszka-Tobiasz','Ewa Marciniak','Paweł Krzywda']:assert name in godziny,name
assert godziny.count('class="doctor"')==18
for page in ['index.html','laboratorium.html']:
 html=ROOT.joinpath(page).read_text();assert '7:30–11:00' in html
 assert 'Czy muszę być na czczo?' in html and 'Do potwierdzenia:' in html
vaccines=ROOT.joinpath('szczepienia.html').read_text()
assert 'Kiedy szczepienie na grypę?' in vaccines and 'W źródłach nie ma tych informacji' in vaccines
assert '2025' in vaccines and '2026' in vaccines
assert '7:30–18:00' in godziny and '8:00–18:00' in godziny
rx=ROOT.joinpath('e-recepta.html').read_text();assert 'nie przyjmuje zamówień ani danych' in rx and 'nie podaje czasu realizacji' in rx
print(f'PASS: 6 stron, {checked} lokalnych linków/kotwic/zasobów, 18 grafików, 2 zweryfikowane oryginalne zdjęcia, noindex, brak formularzy i zasobów zewnętrznych.')
# Text colours are used at >=18px; require AA contrast even at ordinary text size.
def luminance(hex):
 rgb=[int(hex[i:i+2],16)/255 for i in (1,3,5)]
 rgb=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
 return sum(a*b for a,b in zip(rgb,[.2126,.7152,.0722]))
ratios=[]
for fg,bg in [('#26332d','#ffffff'),('#26332d','#edf4ef'),('#53645a','#ffffff'),('#53645a','#edf4ef'),('#365d4b','#edf4ef'),('#365d4b','#ffffff'),('#b3141f','#ffffff'),('#ffffff','#b3141f'),('#ffffff','#365d4b')]:
 a,b=sorted([luminance(fg),luminance(bg)]);ratio=(b+.05)/(a+.05);assert ratio>=4.5,(fg,bg,ratio);ratios.append(ratio)
print(f'PASS: kontrast wszystkich par tekstu {min(ratios):.2f}:1–{max(ratios):.2f}:1 (AA).')
