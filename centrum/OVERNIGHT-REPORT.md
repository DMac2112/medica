# Centrum — raport odświeżenia (2026-10-13, runda 2)

## Zmieniono
- Odświeżono pełny HTML pięciu stron: główna, informacje, kontakt, poz, specjalisci. Użyto handlera SSR z aktualnego `.output` Arsmedica2 (commit `3362c48`), tak jak w poprzednim odświeżeniu; bez ponownego budowania i zmian w repozytorium źródłowym.
- Przeniesiono aktualne moduły JS i CSS oraz źródłowe zdjęcia, dwa PDF-y, favicon i robots.txt. Nowy podgląd zawiera większe pola nawigacji, krótszy komunikat „Rozbieżne godziny POZ.” i telefon rejestracji na pełną szerokość pod godzinami.
- Zachowano `/medica/centrum/` w linkach, zasobach, metadanych, preloadach i routerze po hydratacji. Każda strona ma `noindex, nofollow`; robots.txt blokuje indeksowanie. Starsze zasoby pozostawiono.
- Zmieniono tylko `centrum/`; zastane zmiany w `pytania/` pozostały nietknięte. Nie wykonano commita ani pusha.

## Fakty „do potwierdzenia”
Nie dodano nowych faktów ani oznaczeń; zachowano oznaczenia z aktualnego Arsmedica2:
- Godziny POZ i gabinetu zabiegowego (8:00 / 7:30), brak osobnych godzin rejestracji, aktualność grafików, piątki parzyste/nieparzyste i brak grafiku pielęgniarek oraz położnej.
- Specjaliści: Julia Dobosz / Wiktoria Szczęsna, czwartek / piątek u chirurga naczyniowego, dwa numery masażu i brakujące godziny przyjęć.
- Laboratorium: zakres badań i ceny, NFZ/skierowanie, przygotowanie, odbiór i terminy wyników po weekendach oraz świętach.
- Szczepienia: kalendarz 2026 / tytuł 2025, zakres szczepienia skojarzonego, dostępność, wiek, kwalifikacja i finansowanie.
- Informacje: zapisy do POZ i dokumenty do wizyty, dojazd/parking/wejście, PDF z 2019 r., kompletność RODO i procedur pacjenta oraz oznaczenia projektu grantowego.

## Sprawdzono / niewykonane
- PASS: pięć tras SSR zwraca 200, nieistniejąca trasa 404; HTML odpowiada aktualnemu buildowi po normalizacji ścieżek i znaczników czasu. Sprawdzono 110 lokalnych linków, kotwic i zasobów oraz składnię ośmiu modułów JS. Moduły odpowiadają źródłu poza zmianami ścieżek wdrożenia; CSS, zdjęcia i dokumenty są identyczne bajtowo ze źródłem.
- PASS: noindex/nofollow na wszystkich stronach; brak formularzy i osadzonych iframe. Nie dodano zewnętrznych fontów, trackerów ani nowych zdjęć.
- `git diff --check` wskazuje końcową spację w zmienionej pierwszej linii `informacje/index.html`: pochodzi z zachowanego źródłowego komunikatu o naruszeniu danych. Nie zmieniano tekstu prawnego.
- Niewykonane: wizualna kontrola 360/390 px, pomiar przewijania i widoczności godzin/telefonu, interakcje po hydratacji oraz kontrola konsoli przeglądarki. Próba uruchomienia lokalnego serwera została zablokowana przez sandbox (`Operation not permitted`). Fakty wymagają potwierdzenia przez przychodnię.
