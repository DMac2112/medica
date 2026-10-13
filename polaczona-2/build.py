"""Generate the six static previews. No runtime build or dependencies required."""
from pathlib import Path
from html import escape
import re
ROOT = Path(__file__).resolve().parent
AUDIT = Path('/Users/dom/Websites/arsmedica-nfz/audit/pages')
PHONE = '+48625802252'

def confirm(text):
    return f'<p class="confirm"><strong>Do potwierdzenia:</strong> {text}</p>'
def link(href,text,kind='link'):
    return f'<a class="{kind}" href="{href}">{text}</a>'
def call(text='Zadzwoń do rejestracji'):
    return link('tel:'+PHONE,f'{text}<span class="call-number">62 580 22 52</span>','button')
def qa(question,body,id='',tone=''):
    return f'<section class="question-section {tone}"'+(f' id="{id}"' if id else '')+f'><div class="wrap question-layout"><h2>{question}</h2><div class="answer">{body}</div></div></section>'
def row(name,value,note=''):
    return f'<div><dt>{name}</dt><dd>{value}'+(confirm(note) if note else '')+'</dd></div>'
def header(page):
    tasks=[('Godziny','godziny.html#godziny'),('Lekarze','godziny.html#lekarze'),('Laboratorium','laboratorium.html'),('Szczepienia','szczepienia.html'),('Kontakt i informacje','kontakt.html')]
    nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if page==url.split('#')[0] and '#' not in url else '')+f'>{title}</a>' for title,url in tasks)
    return f'''<a class="skip" href="#main">Przejdź do treści</a>
<header class="header"><div class="wrap brand-row"><a class="brand" href="index.html" aria-label="ARSMEDICA CENTRUM — strona główna"><svg viewBox="0 0 44 44" aria-hidden="true"><path d="M6 36 20 7h5l14 29h-8l-3-7H16l-3 7Z" fill="currentColor"/><path d="M22 14v10m-5-5h10" stroke="white" stroke-width="3"/></svg><span><strong>ARSMEDICA</strong><span>Centrum · Kalisz, Babina 3</span></span></a><span class="preview">Podgląd strony</span></div>
<div class="care-strip"><div class="wrap care-inner"><a class="today" data-today-link href="godziny.html#godziny"><span data-today="label">POZ · poniedziałek–piątek</span><strong data-today="hours">8:00–18:00</strong><span class="today-note" data-today="note">Plan tygodniowy · godziny do potwierdzenia</span></a><a class="phone" href="tel:{PHONE}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 3H4a1 1 0 0 0-1 1c0 9.4 7.6 17 17 17a1 1 0 0 0 1-1v-3l-5-2-2 2a14 14 0 0 1-7-7l2-2-2-5Z"/></svg><span>Rejestracja POZ<strong>62 580 22 52</strong></span></a></div></div>
<nav class="task-nav" aria-label="Najważniejsze sprawy pacjenta"><div class="wrap task-inner">{nav}</div></nav></header>'''
def footer():
    return '''<footer class="footer"><div class="wrap footer-grid"><div><strong class="footer-brand">ARSMEDICA CENTRUM</strong><p>Poradnia Podstawowej Opieki Zdrowotnej<br>ul. Babina 3, 62-800 Kalisz</p><a class="link" href="tel:+48625802252">Rejestracja: 62 580 22 52</a></div><nav aria-label="Pozostałe sprawy"><a href="e-recepta.html">Jak zamówić e-receptę?</a><a href="kontakt.html#nfz">Opieka na NFZ</a><a href="kontakt.html#dokumenty">Dokumenty i prawa pacjenta</a><a href="kontakt.html#komunikaty">Komunikaty o ochronie danych</a><a href="kontakt.html#pomoc">Pomoc poza godzinami POZ</a></nav></div><div class="wrap footer-bottom"><p>Podgląd projektu. Informacje oznaczone „do potwierdzenia” wymagają sprawdzenia w przychodni.</p><a href="#top">Wróć na górę</a></div></footer>'''
def page(filename,title,body):
    ROOT.joinpath(filename).write_text(f'''<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><meta name="description" content="{escape(title)}. ARSMEDICA CENTRUM, Kalisz, Babina 3. Rejestracja: 62 580 22 52."><meta name="theme-color" content="#ffffff"><title>{escape(title)} | ARSMEDICA CENTRUM</title><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head><body id="top">{header(filename)}<main id="main">{body}</main>{footer()}</body></html>''',encoding='utf-8')
def title(name,lead):
    return f'<div class="wrap page-title"><a class="back" href="index.html">Strona główna</a><h1>{name}</h1><p>{lead}</p></div>'

hours = '<dl class="hours-list">'+row('Poradnia POZ na NFZ','<strong>8:00–18:00</strong><span>Poniedziałek–piątek</span>')+row('Gabinet zabiegowy','<strong>8:00–18:00</strong><span>Poniedziałek–piątek</span>')+'</dl>'
hours += confirm('oferta POZ podaje 8:00–18:00, a stopka 7:30–18:00 dla gabinetów. Osobnych godzin rejestracji nie podano. Przed wizytą sprawdź aktualny plan, także w święta.')

# Names and schedules transcribed from audit/pages/oferta-poz.md.
doctors=[
 ('andrzejczak','Paweł Andrzejczak','Internista, medycyna rodzinna',['8:00–13:00','13:00–18:00','8:00–13:00','8:00–13:00','Dni parzyste: 13:00–18:00; nieparzyste: 8:00–18:00']),
 ('lisowski','Piotr Lisowski','Specjalista medycyny rodzinnej',['8:00–13:00','8:00–13:00','13:00–18:00','13:00–18:00','8:00–13:00']),
 ('krawczyk','Agnieszka Krawczyk-Kubisiak','Specjalista medycyny rodzinnej',['11:00–16:00','8:00–13:00','8:00–13:00','8:00–13:00','Dni parzyste: 8:00–13:00; nieparzyste: 11:00–16:00']),
 ('grzeluszka','Irena Grzeluszka-Tobiasz','Pediatra, medycyna rodzinna',['9:00–14:00','9:00–12:30','11:00–16:00','13:00–18:00','9:00–13:00']),
 ('marciniak','Ewa Marciniak','Specjalista medycyny rodzinnej',['8:00–13:00','13:00–18:00','8:00–13:00','8:00–13:00','Dni parzyste: 13:00–18:00; nieparzyste: 8:00–13:00']),
 ('krzywda','Paweł Krzywda','Rezydent medycyny rodzinnej',['','15:00–18:00','','','15:00–18:00'])]
days=['Poniedziałek','Wtorek','Środa','Czwartek','Piątek']
doctor_links='<div class="doctor-links">'+''.join(link('godziny.html#'+slug,name) for slug,name,_,_ in doctors)+'</div>'

home='''<section class="wrap guide-intro"><div class="intro-type"><svg class="conversation" viewBox="0 0 80 80" aria-hidden="true"><path d="M12 5h41c15 0 22 8 22 23v13c0 15-7 22-22 22H34L12 76V5Z" fill="currentColor"/><path d="M31 26c0-14 23-14 23-1 0 9-12 8-12 18" stroke="white" stroke-width="5" fill="none"/><circle cx="42" cy="51" r="3" fill="white"/></svg><h1>W czym możemy pomóc?</h1><p>Godziny, badania, szczepienia.<br>Znajdź odpowiedź na swoje pytanie.</p></div><figure class="intro-photo"><img src="../centrum/assets/reception-Brh0pYck.jpg" alt="Okienko rejestracji w ARSMEDICA CENTRUM" width="800" height="449"><figcaption>Twoja przychodnia przy Babina 3 w Kaliszu.</figcaption></figure></section>'''
home+=qa('Kiedy jest otwarte?',hours+link('godziny.html#godziny','Wszystkie godziny pracy'),'godziny')
home+=qa('Kiedy przyjmuje mój lekarz?','<p>Wybierz nazwisko, aby zobaczyć godziny przyjęć w całym tygodniu.</p>'+doctor_links+link('godziny.html#personel','Pielęgniarki, położna i specjaliści'),'lekarze')
home+=qa('Kiedy jest pobieranie krwi?','<p class="big-answer">7:30–11:00</p><p>Poniedziałek–piątek, w punkcie pobrań przy Babina 3.</p><h3>Czy muszę być na czczo?</h3><p>Zapytaj o przygotowanie do swojego badania przed pobraniem.</p>'+confirm('zasady przygotowania, w tym bycie na czczo. Nie opisano ich w źródłach.')+link('laboratorium.html','Badania, przygotowanie i wyniki'),'laboratorium','green-section')
home+=qa('Kiedy szczepienie na grypę?','<p>Termin i dostępność sprawdź w punkcie szczepień przez rejestrację.</p>'+confirm('szczepienia przeciw grypie: oferta, terminy, wiek i finansowanie. Źródła nie podają tych informacji.')+link('szczepienia.html','Szczepienia dla siebie lub dziecka'),'szczepienia')
home+=qa('Jak załatwić swoją sprawę?','<div class="service-links">'+link('kontakt.html','Gdzie jest przychodnia i jak dojechać?')+link('e-recepta.html','Jak zamówić receptę na stałe leki?')+link('kontakt.html#nfz','Jak skorzystać z opieki na NFZ?')+link('kontakt.html#dokumenty','Gdzie znajdę dokumenty i prawa pacjenta?')+'</div>','informacje')
home+='''<aside class="help-band"><div class="wrap help-layout"><div><h2>Nie wiesz, od czego zacząć?</h2><p>Zadzwoń do rejestracji i zapytaj o swoją sprawę.</p></div>'''+call()+'''</div></aside>'''
page('index.html','Przewodnik pacjenta',home)

# Hours and full team schedules.
godziny=title('Godziny i lekarze','Sprawdź godziny swojej usługi albo wybierz nazwisko lekarza.')
godziny+=qa('O której mogę przyjść?',hours+'<dl class="hours-list">'+row('Punkt pobrań','<strong>7:30–11:00</strong><span>Poniedziałek–piątek</span>')+row('Odbiór wyników','<strong>Następnego dnia od 14:00</strong>','sposób odbioru i termin po piątku lub święcie.')+row('Rejestracja do specjalistów','<strong>8:00–16:00</strong><span>Poniedziałek–piątek</span>'+link('tel:+48500308305','500 308 305'))+'</dl>','godziny')
disclosures=''
for slug,name,specialty,schedule in doctors:
    entries=''.join(row(day,f'<strong>{time}</strong>') for day,time in zip(days,schedule) if time)
    friday=confirm('znaczenie „dni parzystych / nieparzystych” oraz piątkowe zmiany. Ustal swój termin w rejestracji.') if 'Dni parzyste' in schedule[-1] else ''
    disclosures+=f'<details class="doctor" id="{slug}"><summary><span><strong>{name}</strong><span>{specialty}</span></span><span class="expand" aria-hidden="true"></span></summary><div class="disclosure-body"><dl class="schedule">{entries}</dl>{friday}'+link('tel:'+PHONE,'Umów wizytę: 62 580 22 52')+'</div></details>'
godziny+=qa('Kiedy przyjmuje mój lekarz?','<p>Wybierz nazwisko, aby rozwinąć cały tydzień. Wizyty POZ umawiaj w rejestracji.</p>'+confirm('aktualność poniższych grafików, zastępstwa i zmiany w święta.')+disclosures,'lekarze')
godziny+=qa('Kiedy pracują pielęgniarki i położna?','<p>O godziny przyjęć zapytaj w rejestracji.</p>'+confirm('nazwiska i dyżury pielęgniarek oraz położnej. Źródła nie zawierają osobnego grafiku.')+call('Zapytaj o personel'),'personel','green-section')
# Specialist source: start.md and o-nas.md. Never interpret missing times as booked slots.
specialists=[
 ('Ortopeda','dr n. med. Piotr Wojciechowski','Wtorek od 18:00','500 308 305',''),
 ('Neurolog','dr n. med. Karolina Tworek','','500 308 305',''),
 ('Kardiolog','lek. Agata Serwecińska','Poniedziałek','500 308 305','Godziny rozpoczęcia i zakończenia przyjęć.'),
 ('Medycyna pracy i transportu','lek. Piotr Lisowski','Poniedziałek–czwartek','500 308 305','Godziny rozpoczęcia i zakończenia przyjęć.'),
 ('Fizjoterapia uroginekologiczna i urologiczna','mgr Aneta Kliber','','881 693 188',''),
 ('Psychiatra','lek. Jadwiga Liberowicz-Przybył','Poniedziałek i środa','692 685 922','Godziny rozpoczęcia i zakończenia przyjęć.'),
 ('Chirurg naczyniowy','dr n. med. Jarosław Kasperczak','Poniedziałek i czwartek od 16:00','607 051 894','Dni przyjęć: strona „O nas” podaje poniedziałek i piątek.'),
 ('Pulmonolog','lek. Waldemar Bakalarz','Czwartek','500 308 305','Godziny rozpoczęcia i zakończenia przyjęć.'),
 ('Psychologia pracy','mgr Izabela Płucienniczak','Poniedziałek 8:00–15:00; czwartek 12:00–18:00','503 114 595',''),
 ('Psycholog','mgr Justyna Prus-Buczak','','601 775 701',''),
 ('Dietetyk','Julia Dobosz','','791 755 792','Nazwisko: strona „O nas” podaje Julię Dobosz, strona główna Wiktorię Szczęsną.'),
 ('Masaż leczniczy','Gohar Meliksetyan','Poniedziałek–piątek od 12:00','880 683 065','Telefon: strona „O nas” podaje 500 308 305, strona główna 880 683 065.')]
specialist_html=''
for field,name,time,phone,note in specialists:
    body=f'<p>{time}</p>' if time else confirm('godziny przyjęć. Zapytaj pod numerem rejestracji poniżej.')
    body+=confirm(note) if note else ''
    body+=link('tel:+48'+re.sub(r'\D','',phone),'Rejestracja: '+phone)
    specialist_html+=f'<details class="doctor"><summary><span><strong>{field}</strong><span>{name}</span></span><span class="expand" aria-hidden="true"></span></summary><div class="disclosure-body">{body}</div></details>'
godziny+=qa('Jak umówić specjalistę?','<p>Prywatne gabinety mają osobne numery rejestracji. Wybierz specjalność.</p>'+confirm('aktualność zespołu, godzin i telefonów.')+specialist_html,'specjalisci')
godziny+=qa('Gdzie szukać pomocy po zamknięciu?','<p>Źródło wskazuje Wojewódzki Szpital Zespolony w Kaliszu, ul. Poznańska 79, budynek Pogotowia — po 18:00 i w święta.</p>'+link('tel:+48627651654','62 765 16 54')+confirm('aktualne miejsce, telefon i zasady pomocy poza godzinami POZ.')+link('kontakt.html#pomoc','Pomoc poza godzinami i pozostałe kontakty'),'pomoc')
page('godziny.html','Godziny i lekarze',godziny)

lab=title('Laboratorium','Pobranie krwi, przygotowanie i odbiór wyników — po kolei.')
lab+=qa('Kiedy jest pobieranie krwi?','<p class="big-answer">7:30–11:00</p><p>Poniedziałek–piątek.<br>Punkt pobrań w przychodni, ul. Babina 3 w Kaliszu.</p>'+confirm('godziny w święta i ewentualne zmiany planu.')+call('Zapytaj o pobranie'),'pobrania','green-section')
lab+=qa('Czy muszę być na czczo?','<p>Zapytaj rejestrację o przygotowanie do konkretnego badania przed przyjściem.</p>'+confirm('bycie na czczo, jedzenie, picie i przyjmowanie leków przed badaniem. Źródło nie zawiera instrukcji.')+'<div class="ask-note"><h3>O co zapytać przed pobraniem?</h3><ul><li>Czy to badanie wymaga bycia na czczo?</li><li>Jak przygotować się do mojego badania?</li><li>Czy potrzebuję skierowania?</li><li>Czy badanie jest na NFZ czy płatne?</li></ul></div>'+call('Zapytaj o przygotowanie'),'przygotowanie')
lab+=qa('Jakie badania mogę wykonać?','<p>Przychodnia potwierdza możliwość wykonania badań płatnych. Szczegółowej listy nie opublikowano.</p>'+confirm('lista badań, ceny, skierowanie i zakres finansowania przez NFZ. Zapytaj lekarza POZ o badania, które może zlecić.'),'badania')
lab+=qa('Kiedy i jak odbiorę wyniki?','<p class="big-answer smaller">Następnego dnia<br>od 14:00</p><p>Taką godzinę podaje informacja laboratorium.</p>'+confirm('czas oczekiwania na konkretne badanie, termin po piątku i świętach, miejsce i sposób odbioru oraz możliwość dostępu przez internet.')+call('Zapytaj o swoje wyniki'),'wyniki','green-section')
page('laboratorium.html','Laboratorium',lab)

vaccines=title('Szczepienia','Dla siebie lub dziecka. O termin zapytaj w punkcie szczepień przez rejestrację.')
vaccines+=qa('Kiedy szczepienie na grypę?','<p>Sprawdź dostępność i termin przed przyjściem do przychodni.</p>'+confirm('oferta szczepień przeciw grypie, terminy, wiek pacjenta, kwalifikacja i finansowanie. W źródłach nie ma tych informacji.')+call('Zapytaj o szczepienie na grypę'),'grypa','green-section')
vaccines+=qa('Jakie szczepienia są w ofercie?','<p>W ofercie źródłowej wymieniono:</p><dl class="vaccine-list">'+row('Wirusowe zapalenie wątroby','Euvax. Źródło opisuje pełny cykl jako 3 dawki.')+row('Pneumokoki','Prevenar.')+row('Rotawirusy','Rotarix.')+row('Szczepienie skojarzone','Infanrix IPV+Hib.','dokładny zakres. Opis chorób i nazwa preparatu w źródle wymagają sprawdzenia.')+row('Krztusiec','Strona przychodni zawiera informację o szczepieniach dzieci i dorosłych, w tym osób mających kontakt z niemowlętami oraz kobiet w ciąży lub ją planujących.')+'</dl>'+confirm('aktualna dostępność preparatów, wiek, liczba dawek, kwalifikacja i finansowanie. Szczepienie odpowiednie dla Ciebie ustal w punkcie szczepień.'),'oferta')
vaccines+=qa('Który kalendarz szczepień obowiązuje?','<p>Treść strony przychodni wskazuje kalendarz GIS na <strong>2026 rok</strong>. Szczegółowych informacji udziela punkt szczepień.</p>'+confirm('aktualny kalendarz: tytuł źródłowej strony nadal podaje 2025, a jej treść 2026. Źródło nie zawiera rozpiski wieku i dawek.'),'kalendarz')
vaccines+=qa('Jak umówić szczepienie?','<ol class="steps"><li>Zadzwoń do rejestracji i zapytaj o punkt szczepień.</li><li>Powiedz, o jakie szczepienie pytasz i dla kogo.</li><li>Ustal termin, przygotowanie i zasady kwalifikacji.</li></ol>'+confirm('zasady zapisów, wymagane dokumenty i przygotowanie. Powyższa lista pomaga w rozmowie; nie jest potwierdzoną procedurą przychodni.')+call('Zadzwoń w sprawie szczepienia'),'zapisy','green-section')
page('szczepienia.html','Szczepienia',vaccines)

contact=title('Kontakt i dojazd','ARSMEDICA CENTRUM, ul. Babina 3, 62-800 Kalisz.')
contact+=qa('Pod jaki numer zadzwonić?','<div class="contact-lines"><div><h3>Rejestracja POZ</h3>'+link('tel:'+PHONE,'62 580 22 52','contact-number')+'</div><div><h3>Telefon komórkowy</h3>'+link('tel:+48573335284','573 335 284','contact-number')+'</div><div><h3>Rejestracja do specjalistów</h3>'+link('tel:+48500308305','500 308 305','contact-number')+'<p>Poniedziałek–piątek, 8:00–16:00.</p></div></div>'+confirm('osobne godziny rejestracji POZ nie są opublikowane. Niektórzy specjaliści mają inne numery rejestracji.')+link('godziny.html#specjalisci','Telefony poszczególnych specjalistów'),'telefony')
contact+='''<section class="location-section" id="dojazd"><div class="wrap location-layout"><figure><img src="../centrum/assets/hero-clinic-DmIzVco1.jpg" alt="Budynek przychodni ARSMEDICA przy ul. Babina 3 w Kaliszu, widok od ulicy" width="800" height="450" loading="lazy"><figcaption>Budynek przy ul. Babina 3. Zdjęcie z galerii przychodni.</figcaption></figure><div><h2>Jak do nas trafić?</h2><address>ul. Babina 3<br>62-800 Kalisz</address><a class="button secondary" href="https://www.google.com/maps/dir/?api=1&amp;destination=Babina+3%2C+Kalisz" rel="noopener noreferrer">Wyznacz trasę w mapach</a><p>Mapa otworzy się w serwisie Google Maps.</p>'''+confirm('wejście do przychodni, dostępność dla osób z ograniczoną mobilnością, parking i najbliższe przystanki. Przed przyjazdem zapytaj o potrzebną pomoc.')+'</div></div></section>'
contact+=qa('Czy mogę leczyć się na NFZ?','<p>Przychodnia świadczy podstawową opiekę zdrowotną w ramach umowy z NFZ. Przyjmują lekarze rodzinni, internista i pediatra.</p>'+confirm('zasady zapisania do POZ, deklaracja wyboru, dokumenty do wizyty oraz finansowanie konkretnego świadczenia.')+'<h3>Profilaktyka i opieka koordynowana</h3><p>Przychodnia informuje o programach CHUK i „Moje Zdrowie – bilans zdrowia osoby dorosłej” oraz opiece koordynowanej.</p>'+confirm('warunki udziału, dostępność i zapisy do programów. Zapytaj rejestrację lub swojego lekarza.')+call('Zapytaj o opiekę na NFZ'),'nfz')
contact+=qa('Gdzie szukać pomocy po godzinach?','<h3>Opieka nocna i świąteczna</h3><p>Źródło wskazuje Wojewódzki Szpital Zespolony w Kaliszu, ul. Poznańska 79, budynek Pogotowia — po 18:00 i w święta.</p>'+link('tel:+48627651654','62 765 16 54')+confirm('aktualne miejsce, telefon i zasady udzielania pomocy.')+'<h3>Transport sanitarny</h3><p>Art &amp; Med — kontakt podany w informacjach przychodni.</p>'+link('tel:+48625941112','62 594 11 12')+link('tel:+48660703333','660 703 333')+confirm('aktualność telefonów i zasady zamówienia transportu.'),'pomoc','green-section')
contact+=qa('Gdzie znajdę dokumenty?','<div class="service-links">'+link('../centrum/dokumenty/prawa-i-obowiazki-pacjenta-babina.pdf','Prawa i obowiązki pacjenta (PDF)')+link('../centrum/dokumenty/poza-kolejnoscia-babina.pdf','Przyjęcie poza kolejnością (PDF)')+link('e-recepta.html','E-recepta — informacje')+'</div>'+confirm('aktualność dokumentów, w tym PDF z 2019 r., procedura skarg, regulamin oraz zasady udostępniania dokumentacji. Zapytaj rejestrację o aktualne wersje.'),'dokumenty')

# Preserve the clinic's two notices as quoted source text, not as freshly verified statements.
def plain_source(text):
    text=re.sub(r'\r','',text)
    paragraphs=re.split(r'\n\s*\n',text)
    out=[]
    for block in paragraphs:
        block=block.strip()
        if not block or block in ['-','---']: continue
        if re.match(r'^### ',block): out.append('<h3>'+escape(block[4:])+'</h3>')
        else: out.append('<p>'+escape(block.lstrip('- \t')).replace('\n',' ')+'</p>')
    return ''.join(out)
start=AUDIT.joinpath('start.md').read_text()
notice=start.split('### Zawiadomienie o naruszeniu ochrony danych osobowych',1)[1].split('# Zadbaj o zdrowie',1)[0].strip()
news=AUDIT.joinpath('aktualnosci.md').read_text().split('##  Aktualności',1)[1].split('---',1)[0].strip()
contact+=qa('Co oznacza wiadomość o MyDr?','<p>Przychodnia opublikowała dwa komunikaty o ochronie danych. Poniżej zachowano ich treść ze źródeł.</p>'+confirm('aktualność komunikatów i wskazanych w nich kontaktów. Są to cytowane informacje z audytu z 12 października 2026, a nie nowa ocena bezpieczeństwa.')+'<details class="document"><summary>Zawiadomienie o naruszeniu ochrony danych osobowych<span class="expand" aria-hidden="true"></span></summary><div class="disclosure-body source-notice">'+plain_source(notice)+'</div></details><details class="document"><summary>Informacja przychodni z aktualności<span class="expand" aria-hidden="true"></span></summary><div class="disclosure-body source-notice">'+plain_source(news)+'</div></details>','komunikaty')
page('kontakt.html','Kontakt i dojazd',contact)

rx=title('Jak zamówić e-receptę?','Informacje dla pacjentów przyjmujących leki na choroby przewlekłe.')
rx+=qa('Od czego zacząć?','<p>Zadzwoń do rejestracji i zapytaj o aktualny sposób zamówienia recepty na stale przyjmowane leki.</p>'+call('Zapytaj o zamówienie recepty')+confirm('aktualny kanał zamawiania i zasady wystawiania. Ta strona jest podglądem informacji; nie przyjmuje zamówień ani danych pacjentów.'),'zamowienie','green-section')
rx+=qa('Dla kogo jest ta usługa?','<p>Źródło opisuje e-receptę dla pacjentów przyjmujących leki stosowane w leczeniu chorób przewlekłych — na leki przepisane wcześniej przez lekarza, bez konieczności wizyty.</p>'+confirm('czy w Twojej sytuacji potrzebna jest konsultacja i jakie są aktualne warunki wystawienia recepty. Ustal to z przychodnią.'))
rx+=qa('Co przygotować do rozmowy?','<p>Przygotuj nazwę leku, jego postać, dawkę, wielkość opakowania i liczbę opakowań, o które chcesz zapytać. Takie informacje wymienia formularz źródłowy.</p>'+confirm('wymagane informacje i sposób weryfikacji pacjenta. Ustal je w przychodni.')+'<div class="ask-note"><p>Nie wpisuj tu danych ani informacji o leczeniu. Ten podgląd nie zawiera formularza.</p></div>')
rx+=qa('Kiedy otrzymam receptę?','<p>Źródło nie podaje czasu realizacji. Podczas rozmowy zapytaj, kiedy możesz spodziewać się odpowiedzi.</p>'+confirm('czas realizacji, sposób powiadomienia i zasady odbioru. Nie potwierdzamy terminu wystawienia.'))
rx+=qa('Jak odbiorę kod?','<p>Źródło opisuje SMS z kodem e-recepty, który służy do realizacji w aptece.</p>'+confirm('aktualny sposób przekazania kodu i dane kontaktowe potrzebne przychodni. Zapytaj o nie w rejestracji.')+call('Ustal szczegóły e-recepty'),'kod','green-section')
page('e-recepta.html','E-recepta — informacje',rx)
print('Wygenerowano sześć stron statycznych w polaczona-2/.')
