# Raport korekty fact-check — klasyczne

## Zmieniono
- Przywrócono link do istniejącego formularza: https://e-arsmedica.pl/zamow-recepte. Nie dodano formularza ani pól danych pacjenta.
- Podano warunki e-recepty: pacjenci ARSMEDICA, wcześniej przepisane leki na choroby przewlekłe; imię i nazwisko, PESEL, aktualny telefon i prośba o aktualny e-mail; nazwa, forma, ilość substancji czynnej i leku w opakowaniu, 1–5 opakowań, termin odbioru; oświadczenie o nieprzebywaniu w szpitalu, sanatorium, rehabilitacji dziennej lub zakładzie opiekuńczo-leczniczym oraz zgoda na przetwarzanie danych. Usunięto wymyślone godziny obsługi e-recept i telefon jako jedyną drogę zamówienia.
- Uzupełniono TPK 800 137 200: pon.–pt. 18:00–8:00 następnego dnia; weekendy, święta i inne dni ustawowo wolne — całodobowo, zgodnie z przekazanym źródłem. Zachowano telefon opieki nocnej i świątecznej 62 765 16 54, ul. Poznańska 79.
- Dodano źródłową informację o dawce przypominającej przeciw krztuścowi u dorosłych co 10 lat oraz zakupionym sprzęcie: spirometr, EKG, Holter EKG i ciśnieniowy, aparat ultrasonograficzny i mobilne USG. Nie dopisano terminów, cen ani finansowania tych badań.
- Usunięto niepotwierdzoną informację o drukowanej klauzuli RODO w przychodni. Zachowano link do klauzuli online. Layout, CSS, zdjęcia i mechanizm zmiany wyglądu pozostawiono bez zmian.

## „Do potwierdzenia”
- Dodano: standardowe EKG 50 zł w cenniku kontra Holter EKG w podsumowaniu audytu. Nazwę i cenę pozostawiono według szczegółowego cennika; nie przypisano tej ceny Holterowi EKG.
- Zachowano istniejące oznaczenia wszystkich pozostałych konfliktów z tabeli: godziny POZ/gabinetu zabiegowego 8:00 kontra 7:30; dni Jarosława Kasperczaka pon./czw. kontra pon./pt.; Julia Dobosz kontra Wiktoria Szczęsna; telefon masażu 880 683 065 kontra 500 308 305; kalendarz szczepień 2026 kontra tytuł 2025.
- Zachowano wcześniejsze notatki o brakujących informacjach: godziny rejestracji, piątkowy grafik, pielęgniarki i położna, odbiór wyników, przygotowanie i zakres badań oraz dostępność szczepień. Nie zastąpiono ich domysłami.

## Weryfikacja i pozostałe sprawy
- Kontrola statyczna: poprawne zagnieżdżenie HTML, unikalne ID, działające cele linków wewnętrznych, istniejące lokalne zasoby, noindex/nofollow, jeden h1 i brak formularzy danych pacjenta; sprawdzono kompletność korekt treści.
- `node --check` obu własnych plików JS i `git diff --check -- klasyczne` przeszły. Projekt statyczny nie ma buildu.
- Wszystkie punkty fact-check dotyczące tej wersji zaadresowano. Rozbieżności źródłowe wymagają potwierdzenia przez przychodnię.
- Nie wykonano wizualnej kontroli mobilnej: środowisko blokuje lokalny serwer, a narzędzie przeglądarki wymaga niedostępnego zatwierdzenia. Nie zmieniano CSS.
- Zmieniono wyłącznie `klasyczne/index.html` i dodano ten raport. Nie wykonano git commit ani git push; istniejące zmiany w `pytania/` pozostawiono nietknięte.
