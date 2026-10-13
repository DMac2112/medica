# Centrum — raport odświeżenia (2026-10-13)

## Zmieniono
- Odświeżono stronę główną i wszystkie podstrony: informacje, kontakt, poz, specjalisci. Nowy build Arsmedica2 nie zawiera dodatkowych tras.
- Wygenerowano pełny HTML przez handler SSR z istniejącego `.output` Arsmedica2 (726547c), bez ponownego budowania ani zmian w źródłowym repozytorium. Przeniesiono aktualne skrypty, CSS, oryginalne zdjęcia i dwa PDF-y.
- Zachowano `/medica/centrum/` w routerze, modułach, preloadach, obrazach, dokumentach, faviconie i metadanych. Wszystkie strony mają `noindex, nofollow`; robots.txt blokuje indeksowanie. Nowe strony nie ładują zewnętrznych fontów ani osadzonej mapy.
- Zmieniono tylko `centrum/`. Starsze, nieużywane zasoby pozostawiono; nie usuwano cudzych plików. Bez commita i pusha.

## „do potwierdzenia”
Nie dodawano nowych faktów ani oznaczeń; zachowano widoczne uwagi z aktualnego Arsmedica2:
- Godziny POZ i gabinetu zabiegowego (8:00 / 7:30), osobne godziny rejestracji, aktualność grafików i piątki parzyste/nieparzyste, brak grafiku pielęgniarek i położnej.
- Specjaliści: Julia Dobosz / Wiktoria Szczęsna, czwartek / piątek u chirurga naczyniowego, dwa numery masażu, brakujące godziny przyjęć.
- Laboratorium: zakres badań i ceny, NFZ/skierowanie, przygotowanie oraz odbiór i terminy wyników po weekendach i świętach.
- Szczepienia: kalendarz 2026 / tytuł 2025, zakres szczepienia skojarzonego, dostępność, wiek, kwalifikacja i finansowanie.
- Informacje: zapisy do POZ i dokumenty do wizyty, dojazd/parking/wejście, PDF z 2019 r., kompletność RODO i procedur pacjenta, oznaczenia projektu grantowego.

## Sprawdzono / niewykonane
- PASS: 5 tras SSR — HTTP 200; nieistniejąca trasa — 404. HTML wszystkich stron odpowiada źródłowemu buildowi po normalizacji ścieżek wdrożenia i znaczników czasu.
- PASS: 110 lokalnych linków, kotwic i zasobów; składnia 8 nowych modułów JS. CSS, zdjęcia, PDF-y, favicon i robots.txt są identyczne bajtowo ze źródłem; zdjęcia odpowiadają wykazowi `hub/image-sources.json`.
- `git diff --check` zgłasza 15 końcowych spacji w skopiowanym, źródłowym tekście komunikatu o naruszeniu danych (`informacje`). Tekstu prawnego nie zmieniano.
- Niewykonane: wizualna kontrola 360/390 px, interakcje po hydratacji i konsola przeglądarki. Narzędzie Playwright wymaga zgody, której polityka tej sesji nie dopuszcza; lokalny serwer jest blokowany przez sandbox (`EPERM`).
- Fakty wymagające potwierdzenia przez przychodnię pozostają oznaczone; podgląd nie zbiera danych pacjentów.
