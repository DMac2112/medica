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
