# Raport — polaczona-2

## Co zmieniono
Nowa wersja statyczna: strona główna, Godziny i lekarze, Laboratorium, Szczepienia, Kontakt i dojazd oraz e-recepta. Własne CSS/JS, favicon i robots.txt. HTML działa bez budowania; build.py służy wyłącznie do regenerowania stron.

Spokojny przewodnik po pytaniach pacjentów. Pięć priorytetów zachowuje kolejność briefu; godziny POZ i telefon są na górze, wszystkie skróty widoczne bez otwierania menu. Treść 20px, uwagi minimum 18px, cele dotykowe minimum 48px. Odpowiedzi podstawowe od razu widoczne; rozwijanie tylko długich grafików i komunikatów.

Z klasycznej wersji: komplet grafików i proste details. Z centrum: pięć bezpośrednich skrótów. Z Next: oddzielne godziny usług, strefa Europe/Warsaw i jawne braki danych. Od polaczona-1 różni ją biały przewodnik pytań, bez czerwonej tablicy i osi czasu. Ryzyko estetyczne: pytania w skali nagłówków oraz czerwony znak rozmowy nawiązujący do okienka rejestracji. Czerwień #b3141f, stonowana zieleń, lokalny Bricolage Grotesque i Arial.

Dwa oryginalne zdjęcia przez względne ścieżki; hashe zgodne z hub/image-sources.json. Zachowane dwa komunikaty MyDr z audytu i linki do lokalnych PDF. Bez formularzy, danych pacjenta, trackerów, zewnętrznych fontów i CDN. Plan dnia nie udaje dostępności wizyt; bez JS widoczny plan tygodniowy.

## „Do potwierdzenia”
- **Godziny i zespół:** 8:00 vs 7:30, osobne godziny rejestracji, aktualność grafików, piątki parzyste/nieparzyste, zastępstwa i święta; pielęgniarki i położna; specjalistyczne grafiki/telefony, czwartek vs piątek chirurga, Julia Dobosz vs Wiktoria Szczęsna, dwa numery masażu.
- **Laboratorium:** badania, ceny, skierowanie i NFZ; przygotowanie, w tym bycie na czczo; wyniki po piątku/świętach, terminy konkretnych badań, odbiór i dostęp online.
- **Szczepienia:** oferta i terminy grypy — brak w źródle; kalendarz 2026 vs 2025, zakres preparatu skojarzonego, dostępność, wiek, dawki, kwalifikacja, finansowanie i zapisy.
- **Kontakt i dokumenty:** wejście, dostępność, parking/przystanki, zasady POZ i profilaktyki, aktualność pomocy po godzinach i transportu, PDF z 2019 r., skargi/dokumentacja i aktualność komunikatów.
- **E-recepta:** aktualny kanał i zasady zamówienia, wymagane informacje, konsultacja, czas realizacji, powiadomienie i odbiór kodu. Podgląd nie przyjmuje zamówień.

## Sprawdzenie i niewykonane
PASS: 5/5 testów planu dnia (dzień roboczy, weekend, święta, granica dnia w Warszawie, brak pozornego statusu wizyt). Składnia JS poprawna. Sześć stron, 128 lokalnych linków/kotwic/zasobów, 18 rozwijanych grafików, jeden H1 na stronie, noindex/nofollow, brak formularzy/zasobów zewnętrznych. Kontrast używanych par tekstu: 5,63:1–13,18:1.

**Pozostało:** wizualna kontrola 360/390px i desktopu, rzeczywiste przepełnienia, klawiatura i interakcje w przeglądarce. Sandbox odmawia lokalnego serwera (EPERM); Playwright wymaga niedostępnej zgody; Computer Use odmawia dostępu do Chrome. Screenshotów nie wykonano. CSS przygotowany na 360px, lecz zachowania mobilnego nie przedstawiam jako zweryfikowanego wizualnie.

Fakty oznaczone powyżej wymagają potwierdzenia przez przychodnię. Nic nie wdrażano. Zmiany wyłącznie w polaczona-2/. Bez git commit i git push.
