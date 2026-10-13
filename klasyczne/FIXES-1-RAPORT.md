# Klasyczna — poprawki FIXES-1

- Zmniejszono mobilny h1 do 24 px, aby ograniczyć zawijanie do 1–2 wierszy przy 390 px; tekst pozostaje bez zmian.
- Na ekranach do 720 px przełącznik „Wygląd” znajduje się w normalnym układzie pod stopką. Zachowano rozwijanie i wybór stylu oraz koloru; przełącznik nie nakłada się na treść.
- Cztery główne skróty mają jednakowe wysokości, minimum 56 px, oraz wypełnienie istniejącym akcentem marki (domyślnie #b01f2c). Piąty skrót pozostaje pomocniczy.
- Usunięto dekoracyjne podkreślenia nagłówków sekcji i odstęp przeznaczony na te ozdoby.

**„Do potwierdzenia”:** nie dodano nowych oznaczeń ani nie zmieniano faktów. Zachowano dotychczasowe uwagi dotyczące godzin, grafików i danych zespołu, laboratorium, szczepień oraz e-recepty; szczegóły są w RAPORT.md.

**Weryfikacja:** brak buildu w statycznym projekcie. `git diff --check` i `node --check klasyczne/js/app.js` przeszły. Kontrola statyczna potwierdziła zachowanie treści strony, noindex/nofollow, celów nawigacji i istniejących lokalnych zasobów.

**Pozostało:** wizualne sprawdzenie 360/390/1440 px, pomiar liczby wierszy h1, przepełnienia i reguły 3 sekund oraz działanie przełącznika w rzeczywistej przeglądarce. Sandbox blokuje serwer lokalny (`listen EPERM`); Playwright wymaga zgody, której bieżąca polityka nie pozwala uzyskać. Wyniku wizualnego nie potwierdzono.

Zmieniono wyłącznie klasyczne/. Bez git commit i git push.

## Przegląd czterech uwag hooka

- Trzy `side-tab`: zachowano odziedziczone akcenty informacji pomocniczych, faktów e-recepty i kart programów NFZ zgodnie z wymaganiem utrzymania charakteru wersji. Istniejące wyjątki są zapisane wyłącznie dla index.html w klasyczne/.impeccable/config.json.
- Jeden `cramped-padding`: fałszywy alarm dla faktów e-recepty. Reguły CSS zapewniają co najmniej 19,2 px poziomego odsunięcia tekstu, ponad wymagane 8 px. Zachowano istniejący wyjątek ograniczony do index.html.
- Nie dodano nowych wyjątków ani poprawek wyglądu. Skan uruchomiony z klasyczne/ respektuje zapisane wyjątki i nie zgłasza tych czterech uwag. Pozostają dwie uwagi informacyjne dotyczące odziedziczonego pasiastego tła i interpunkcji, poza zakresem FIXES-1.
