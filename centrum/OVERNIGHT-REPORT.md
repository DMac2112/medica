# Centrum — raport odświeżenia (2026-10-13, runda 3)

## Zmieniono
- Odświeżono wszystkie 5 stron (główna, informacje, kontakt, POZ, specjaliści) z aktualnego handlera SSR `.output` Arsmedica2, commit `319fa20`, bez przebudowy ani zmian w źródle. Zachowano dotychczasowy sposób odświeżenia, układ i zdjęcia.
- Przeniesiono aktualne moduły JS, CSS i zasoby publiczne; starsze zasoby pozostawiono. Zachowano `/medica/centrum/` w HTML, metadanych, zasobach, preloadach i routerze po hydratacji oraz `noindex, nofollow` na każdej stronie i blokadę robots.txt.
- Podgląd zawiera poprawki fact-checku: godziny opisane jako POZ, ograniczony zakres rejestracji centralnej specjalistów, źródłowy link i wymagania e-recepty, TPK i pomoc po godzinach, informację o krztuścu oraz wyposażeniu z grantu. Nie dodano formularza zbierającego dane.
- Zmieniono wyłącznie `centrum/`. Zastaną zmianę w `pytania/` pozostawiono nietkniętą. Bez commita i pusha.

## Fakty „do potwierdzenia”
Przeniesiono oznaczenia z aktualnego źródła; nie dopisywano własnych faktów:
- Godziny POZ i gabinetu zabiegowego (8:00 / 7:30), brak osobnych godzin rejestracji; uwaga o rozbieżności jest teraz w każdej stopce. Aktualność grafików, piątki parzyste/nieparzyste oraz brak grafiku pielęgniarek i położnej.
- Specjaliści: Julia Dobosz / Wiktoria Szczęsna, czwartek / piątek u chirurga naczyniowego, dwa numery masażu oraz nieopublikowane godziny przyjęć.
- Laboratorium: zakres badań i ceny, NFZ/skierowanie, przygotowanie, sposób i terminy odbioru wyników, w tym po weekendach i świętach.
- Szczepienia: kalendarz 2026 / tytuł 2025, zakres szczepienia skojarzonego, dostępność, wiek, kwalifikacja i finansowanie.
- Informacje: zapisy do POZ i dokumenty do wizyty, dojazd/parking/wejście, aktualność PDF z 2019 r., kompletność RODO i procedur pacjenta oraz oznaczenia projektu grantowego.

## Sprawdzono / niewykonane
- PASS: 5 tras SSR zwraca 200, nieistniejąca trasa 404. Każdy HTML odpowiada aktualnemu buildowi po normalizacji ścieżek i znaczników czasu. Sprawdzono 110 lokalnych linków, kotwic i zasobów oraz składnię 8 modułów JS. CSS, zdjęcia, PDF-y, favicon i robots.txt są identyczne bajtowo ze źródłem.
- PASS: noindex/nofollow, router i prefiks preloadów; brak formularzy, iframe i zewnętrznych fontów/CDN/Google Analytics w aktualnym HTML. Sprawdzono obecność nowych treści fact-checku. Hashe wszystkich 226 śledzonych plików poza `centrum/` pozostały bez zmian.
- `git diff --check`: końcowa spacja w pierwszej linii `informacje/index.html` pochodzi z zachowanego źródłowego komunikatu o naruszeniu danych; pozostawiono ją, aby zachować zgodność ze źródłem.
- Niewykonane: kontrola wizualna 360/390 px, pomiar przewijania i widoczności godzin/telefonu, interakcje po hydratacji i konsola przeglądarki. Sandbox odrzucił próbę otwarcia lokalnego portu (`Operation not permitted`). Dane oznaczone „do potwierdzenia” wymagają potwierdzenia przez przychodnię.
