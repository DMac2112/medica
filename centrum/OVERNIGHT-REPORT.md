# Centrum — raport odświeżenia (2026-10-14)

## Zmieniono
- Odświeżono wszystkie 5 stron (główna, informacje, kontakt, POZ, specjaliści) przez aktualny handler SSR `.output/server/index.mjs` Arsmedica2, jak przy poprzednich odświeżeniach. Źródło: commit `646248a`, build z 14 października; bez przebudowy ani zmian w Arsmedica2.
- Skopiowano aktualne JS, CSS i zasoby publiczne; starsze zasoby pozostawiono. Zachowano `/medica/centrum/` w HTML, zasobach, metadanych, routerze i preloadach oraz `noindex, nofollow`, robots.txt i prefiks w `_headers`.
- Przeniesiono źródłowy link „← Wszystkie wersje Arsmedica” na każdej stronie. W statycznym HTML: `../` na głównej, `../../` na podstronach; oba prowadzą do `/medica/`. Kod źródłowy oblicza powrót po hydratacji na podstawie ścieżki i prefiksu routera.
- Zmieniono wyłącznie `centrum/`. Bez git commit i git push.

## Fakty „do potwierdzenia”
Nie dodano nowych faktów ani nowych oznaczeń; zachowano istniejące oznaczenia ze źródła:
- Godziny POZ i gabinetu zabiegowego (8:00 / 7:30), osobne godziny rejestracji; aktualność grafików, piątki parzyste/nieparzyste, brak grafiku pielęgniarek i położnej.
- Specjaliści: Julia Dobosz / Wiktoria Szczęsna, czwartek / piątek u chirurga naczyniowego, rozbieżne numery masażu i nieopublikowane godziny.
- Laboratorium: zakres i ceny badań, NFZ/skierowanie, przygotowanie oraz sposób i terminy odbioru wyników.
- Szczepienia: kalendarz 2026 / tytuł 2025, zakres szczepienia skojarzonego, dostępność, wiek, kwalifikacja i finansowanie.
- Informacje: zapisy do POZ i dokumenty do wizyty, dojazd/parking/wejście, aktualność PDF z 2019 r., kompletność RODO i procedur pacjenta oraz oznaczenia projektu grantowego.

## Sprawdzono / niewykonane
- PASS: 5 tras SSR zwraca 200; nieistniejąca trasa 404. Każdy HTML i moduł JS odpowiada aktualnemu buildowi po odwróceniu zmian wdrożeniowych. Pozostałe zasoby są identyczne bajtowo ze źródłem, poza świadomie dostosowanym `_headers`.
- PASS: 110 lokalnych linków, kotwic i zasobów; składnia 8 modułów JS i 27 odwołań do zależności; noindex/nofollow, prefiks routera i preloadów, powrót do katalogu na 5 stronach. Brak formularzy, iframe, zewnętrznych fontów/CDN/Google Analytics w aktualnym HTML. Hashe wszystkich 228 plików poza `centrum/` pozostały bez zmian.
- `git diff --check`: jedna końcowa spacja w pierwszej linii `informacje/index.html` pochodzi ze źródłowego komunikatu o naruszeniu danych; zachowano zgodność ze źródłem, jak poprzednio.
- Niewykonane: kontrola wizualna 360/390 px, przewijanie, widoczność godzin/telefonu, interakcje po hydratacji i konsola przeglądarki. Próba uruchomienia lokalnego serwera została zablokowana przez sandbox (`Operation not permitted`). Dane oznaczone „do potwierdzenia” nadal wymagają potwierdzenia przez przychodnię.
