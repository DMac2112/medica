# Raport — polaczona-1

## Co powstało
Nowa, samodzielna wersja statyczna: `index.html`, `godziny.html`, `laboratorium.html`, `szczepienia.html`, `kontakt.html`, `e-recepta.html`. Własne CSS, JS i favicon. Strony działają bez procesu budowania; `build.py` służy tylko do ponownego wygenerowania HTML.

Strona główna jest tablicą „Dziś w przychodni”. JavaScript oblicza stan POZ, osobno pobrania i dzisiejszy grafik w strefie Europe/Warsaw. Odświeża tablicę co minutę i po powrocie do karty. Rozróżnia przed otwarciem, godziny pracy, po zamknięciu, weekend i święto. To plan z zegara urządzenia, nie system informacji o obecności ani rezerwacja. W święta nie pokazuje zwykłych dyżurów; wyjątki wymagają potwierdzenia. Bez JS są godziny tygodniowe i rozwijane grafiki wszystkich sześciu lekarzy. Nie interpretuje niejasnych piątków parzystych/nieparzystych.

Mashup: z klasycznej wersji czytelność i pełny grafik; z centrum szybkie skróty do spraw pacjenta; z Next rozdzielenie godzin usług i jawne braki danych. Ryzyko estetyczne: duża czerwona tablica oraz proporcjonalne paski godzin przyjęć zamiast promocyjnego hero. Czerwień #b3141f z Next, stonowana zieleń, biel, lokalne Public Sans i Archivo. Zdjęcie rejestracji użyte względną ścieżką z centrum; SHA-256 zgodny z hub/image-sources.json.

Zachowano oba komunikaty MyDr z tekstami audytu, dokumenty PDF i informacje NFZ. Bez formularzy, PESEL-u, trackerów, zewnętrznych fontów/CDN. Wszystkie strony mają noindex/nofollow. Edycje wyłącznie w polaczona-1/. Bez git commit i git push.

## Widocznie oznaczone „do potwierdzenia”
- **Godziny i zespół:** POZ/gabinet zabiegowy 8:00 vs 7:30, osobne godziny rejestracji, aktualność grafików, piątkowe zmiany, święta/zastępstwa, pielęgniarki i położna. Specjaliści: aktualność godzin/telefonów, czwartek vs piątek chirurga, Wiktoria Szczęsna vs Julia Dobosz, dwa telefony do masażu.
- **Laboratorium:** lista badań, skierowanie/NFZ, ceny, przygotowanie i bycie na czczo, szczegółowe terminy i sposób odbioru wyników, internet, piątki i święta.
- **Szczepienia:** kalendarz 2026 vs tytuł 2025, dostępność, zakres szczepienia skojarzonego, dawki, wiek, finansowanie, kwalifikacja i zapisy, szczegóły krztuśca.
- **Kontakt/NFZ/dokumenty:** wejście, dostępność i parking, zasady zapisów do POZ/programów, wymagane dokumenty, aktualność PDF z 2019 r., skargi/regulamin/dokumentacja, aktualność pomocy po godzinach, identyfikatory firmy, e-mail i kontakt ds. dostępności.
- **E-recepta:** aktualny kanał, czas realizacji, zasady wystawiania i odbiór kodu; bezpieczeństwo dotychczasowego formularza przed wdrożeniem.

## Sprawdzenie i ograniczenia
`node --test polaczona-1/tests/schedule.test.cjs`: 6/6 zaliczone. `python3 polaczona-1/tests/verify.py`: sześć stron, lokalne linki/kotwice/zasoby, noindex, jeden H1, brak formularzy i zasobów zewnętrznych, grafiki bez JS, dwa komunikaty i hash zdjęcia — zaliczone. `node --check polaczona-1/app.js`: zaliczone. Kontrast tekstu dla używanych par kolorów 5,74:1–14,31:1.

Detektor Impeccable uruchomiony raz: cztery ostrzeżenia. Poprawiono odstępy tła kontaktowego i interlinię nagłówków komunikatów. Ostrzeżenia o czerwonych krawędziach dotyczą pełnej szerokości headera/stopki, nie zaokrąglonych kart.

**Pozostało:** wizualny przegląd 360/390px i desktopu, klawiatury oraz kontrola przepełnień w rzeczywistej przeglądarce. Sandbox odmówił uruchomienia lokalnego serwera i Chromium, a narzędzia Playwright wymagały niedostępnej zgody. Nie wykonano screenshotów; zachowania mobilnego nie przedstawiam jako zweryfikowanego. Nie wdrażano serwisu ani backendu. Fakty oznaczone powyżej wymagają odpowiedzi przychodni.

## Runda poprawek 1 — 2026-10-13
- Nagłówek mobilny: telefon ma własny pełny wiersz, tekst 20–22px i cel minimum 48px; marka nie konkuruje z numerem o szerokość.
- Zamknięcie POZ: pełne zdanie wskazuje dziś, jutro lub datę najbliższego dnia pracy według grafiku, z pominięciem weekendów i świąt. W święto godziny pozostają do potwierdzenia. Uwagi „do potwierdzenia” są neutralne, bez czerwonych wyróżnień.
- Lekarze: każdy ma „dziś” i źródłowe godziny; usunięto powtarzane „Przyjęcia później dzisiaj”. Pozostał status trwających/zakończonych przyjęć i niejasnych piątków.
- Początek sekcji laboratorium podaje pobrania pn.–pt. 7:30–11:00; początek szczepień wskazuje punkt szczepień jako miejsce uzyskania szczegółów kalendarza.

**Do potwierdzenia:** bez nowych wymyślonych faktów. Zachowano wszystkie wcześniejsze oznaczenia, zwłaszcza POZ 8:00 vs 7:30, zastępstwa/święta, piątkowe zmiany, odbiór wyników i kalendarz 2026 vs 2025. Pełna lista jest powyżej.

**Weryfikacja:** `python3 polaczona-1/build.py` zakończone poprawnie; 7/7 testów grafiku; kontrola wszystkich sześciu stron i kontrastów; składnia obu plików JS; wykonanie app.js z atrapą DOM dla wtorku przed otwarciem, wtorku podczas przyjęć i niejasnego piątku — zaliczone.

**Niewykonane:** przegląd w przeglądarce 360/390/1440px, screenshoty i pomiar przepełnień. Sandbox blokuje lokalny serwer (Operation not permitted), a narzędzie Playwright wymaga zgody niedostępnej przy polityce „never”. Zachowanie mobilne nie jest wizualnie zweryfikowane. Nie zmieniano innych wersji ani mechanizmu „Wygląd”; nie uruchamiano git commit ani git push.

## Korekta po FACTCHECK — 2026-10-13

- **Zmieniono:** pełne warunki e-recepty: leki wcześniej przepisane na choroby przewlekłe; imię i nazwisko, PESEL, aktualny telefon i prośba o e-mail (pole bez oznaczenia obowiązkowości); dane każdego leku, 1–5 opakowań, żądany termin odbioru; oświadczenie o nieprzebywaniu w szpitalu, sanatorium, na rehabilitacji dziennej ani w zakładzie opiekuńczo-leczniczym; zgoda na przetwarzanie danych. Zachowano SMS i realizację w dowolnej aptece. Wyraźny link do https://e-arsmedica.pl/zamow-recepte; bez lokalnego formularza. Usunięto kierowanie do telefonu jako koniecznego kroku zamawiania oraz ogólne zastrzeżenia o kanale i warunkach, które źródło opisuje.
- **Uzupełniono:** na stronie głównej, godzinach i kontakcie TPK 800 137 200 (bezpłatny), pn.–pt. 18:00–8:00 następnego dnia, weekendy, święta i inne dni ustawowo wolne — całodobowo. Zachowano opiekę nocną i świąteczną: WSZ Kalisz, Poznańska 79, tel. 62 765 16 54. Dodano źródłowy odstęp dawek przypominających przeciw krztuścowi u dorosłych: co 10 lat; wyposażenie z grantu: spirometr, EKG, Holter EKG/ciśnieniowy, aparat USG i mobilne USG. Doprecyzowano zakres centralnej rejestracji specjalistów.
- **Do potwierdzenia:** zachowano pięć konfliktów z fact-checku: POZ/gabinet zabiegowy 8:00 vs 7:30; chirurg Kasperczak czwartek vs piątek; Wiktoria Szczęsna vs Julia Dobosz; masaż 880 683 065 vs 500 308 305; kalendarz 2026 vs tytuł 2025. Nie znaleziono kolejnych nieoznaczonych konfliktów dotyczących tej wersji. W e-recepcie pozostawiono tylko nieopublikowany czas realizacji; pozostałe wcześniejsze uwagi o brakujących informacjach na innych stronach zachowano.
- **Sprawdzenie:** build.py zakończony poprawnie; verify.py — 6 stron, linki/kotwice, noindex, brak formularzy i zewnętrznych zasobów, oryginalne zdjęcie, kontrast — zaliczone; 7/7 testów grafiku; składnia app.js i schedule.js poprawna; kontrola obecności wszystkich uzupełnień i zachowania pięciu oznaczeń konfliktów — zaliczona. CSS, układ, zdjęcia i logika tablicy bez zmian.
- **Niewykonane:** bez nowego przeglądu wizualnego i pomiaru przepełnień w przeglądarce. Potwierdzenie rozbieżności pozostaje po stronie przychodni. Treści zgodne z dostarczonym snapshotem audit/pages i AUDIT.md; nie weryfikowano ponownie aktualności usług na żywo. Edycje wyłącznie polaczona-1/; bez git commit i git push.
