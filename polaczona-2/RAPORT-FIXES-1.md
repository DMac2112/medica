# polaczona-2 — poprawki FIXES-1

## Zmieniono
- Hero: bardziej wyrównane kolumny, odstęp 48px zamiast 80px, mniejsze wcięcie tekstu. Nagłówek 32px na telefonie, do 64px na desktopie; celem są dwie linie przy 390px.
- Pas godzin: jawne 20px dla tekstu, przypis 18px; same godziny pozostają większe.
- Nawigacja: jasne zielone wypełnienie i białe odstępy zamiast cienkich obrysów.
- Linki w odpowiedziach: pełna szerokość, minimum 56px wysokości, wypełnienie i podkreślenie dopiero przy najechaniu. Zachowano treści, adresy linków i funkcje; przełącznika „Wygląd” w hubie nie zmieniano.

## Fakty „do potwierdzenia”
Nie dodano ani nie zmieniono faktów lub oznaczeń. Zachowano istniejące uwagi: rozbieżne godziny POZ/gabinetów i brak osobnych godzin rejestracji; aktualność grafików i niejasności specjalistów; przygotowanie, zakres i wyniki badań; oferta i finansowanie szczepień oraz kalendarz 2025/2026; zasady kontaktu, dokumentów i e-recepty. Szczegółowa lista: RAPORT.md.

## Weryfikacja i pozostałe
Regeneracja przez `python3 polaczona-2/build.py` zakończona poprawnie; HTML bez zmian. PASS: kontrola 6 stron, 128 lokalnych linków/kotwic/zasobów, oryginalne zdjęcia, noindex, brak formularzy i zewnętrznych zasobów, kontrast AA; 5/5 testów planu dnia; składnia JS i `git diff --check`.

Pozostała kontrola wizualna przy 360/390/1440px, w tym rzeczywistego łamania nagłówka i przepełnień. Serwer lokalny zablokowany przez sandbox (`listen EPERM`), Playwright wymaga zgody niedostępnej przy polityce `never`. Nie przedstawiam tych widoków jako zweryfikowanych.

Zmiany wyłącznie w polaczona-2/. Bez git commit i git push.
