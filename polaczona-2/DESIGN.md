# ARSMEDICA — przewodnik pacjenta

## Brief i decyzja
Samodzielny podgląd statyczny dla pacjentów 60+, zwłaszcza na telefonie. Zlecony kierunek i realizacja określają projekt: nie potrzeba kolejnej rundy wyboru. Tylko polaczona-2/, bez commit/push. Sześć stron, własny CSS i JS, zasoby względne. Fakty wyłącznie z audytu 12.10.2026.

## Synteza po przeczytaniu wersji
- Klasyczne: pełny tydzień w prostych, rozwijanych grafikach; zaufanie wynika z czytelnej informacji.
- Centrum: pięć najważniejszych spraw stale dostępnych bez szukania menu.
- Next src: godziny każdej usługi osobno, obliczenie dnia w Europe/Warsaw, uczciwe braki danych.
- Polaczona-1: czerwona tablica dnia i osie czasu. Tutaj inny pomysł: biały przewodnik, pytanie obok odpowiedzi; bez osi i bez czerwonego hero.

## System i ryzyko estetyczne
Kolory: czerwień marki #b3141f (Next styles.css), zieleń #365d4b, jasna zieleń #edf4ef, biel #ffffff, tekst #26332d, pomocniczy #53645a. Nagłówki: lokalny Bricolage Grotesque 600, tekst Arial 20px (minimum 18px także przypisy). Lewostronne wyrównanie, szerokość odpowiedzi ok. 58 znaków, minimum 48px na dotyk.
Ryzyko: pytania pacjentów zyskują skalę głównego nagłówka, a jeden duży czerwony znak rozmowy przy tytule nawiązuje do pytania przy okienku rejestracji. Rezygnacja z promocyjnego hero i kafelków. Wyróżnik typograficzny, reszta spokojna. Zieleń służy odpowiedziom i przygotowaniu do wizyty; czerwień orientacji i telefonowi.

## Układ
Telefon: marka / dzisiejszy plan POZ + telefon / pięć skrótów / przewodnik pytań w kolejności briefu / zdjęcie prawdziwej rejestracji i kontakt / dokumenty w stopce.
Desktop: godziny i telefon w jednym poziomym pasie; szeroka nawigacja; pytania po lewej, odpowiedzi po prawej. Bez tabel przewijanych poziomo na telefonie.

## Przegląd przeciw szablonom
Odrzucono katalog jednakowych kart FAQ. Zamiast tego otwarte odpowiedzi o różnej strukturze: lista godzin, wejście do grafiku, pas pobrań, odpowiedź o szczepieniach, przewodnik spraw. Rozwijane elementy tylko dla długich grafików i dokumentów. Bez ozdobnych liczb, gradientów, pigułek, neonów, serifów i automatycznych animacji.

## Sprawdzenie
1. [x] Przeczytać brief, audyt i wszystkie wersje; zdefiniować kierunek.
2. [x] Zbudować sześć stron i oznaczyć niepewne dane.
3. [x] Sprawdzić linki, fakty, JS i kontrast. Widoki 360/390px i desktop zablokowane przez narzędzia; ograniczenie opisane w raporcie.
4. [x] Zapisać krótki raport, w tym niewykonane kontrole.
