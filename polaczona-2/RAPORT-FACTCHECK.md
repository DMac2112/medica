# polaczona-2 — poprawki po FACTCHECK

## Zmieniono
- E-recepta: przywrócono link do https://e-arsmedica.pl/zamow-recepte zamiast kierowania wyłącznie do telefonu. Opisano leki przewlekłe przepisane wcześniej, wymagane dane (imię i nazwisko, PESEL, aktualny telefon), prośbę o aktualny e-mail, dane leku, wybór 1–5 opakowań i termin odbioru. Dodano wymagane oświadczenie o nieprzebywaniu w szpitalu, sanatorium, rehabilitacji dziennej ani zakładzie opiekuńczo-leczniczym oraz zgodę na przetwarzanie danych. Zachowano SMS z kodem i brak gwarantowanego czasu realizacji. Nie zbudowano formularza.
- Pomoc poza POZ na stronach godzin i kontaktu: szpital przy Poznańskiej 79, tel. 62 765 16 54; TPK 800 137 200, pon.–pt. 18:00–8:00, weekendy, święta i inne dni ustawowo wolne całodobowo, zgodnie z warto-wiedziec.md. Usunięto szczegół „budynek Pogotowia”, którego wskazana strona źródłowa nie potwierdza.
- Szczepienia: dodano wskazany w start.md odstęp 10 lat między dawkami przypominającymi przeciw krztuścowi dla dorosłych.
- Kontakt: dodano wyposażenie opisane w projekt-grantowy-pn.md (spirometr, EKG, Holter EKG i ciśnieniowy, aparaty USG) oraz link do opisu projektu. Nie przypisano sprzętowi cen ani zasad dostępności badań.
- Poprawiono generator build.py i wygenerowane strony. Zachowano CSS, układ, zdjęcia, nagłówek i nawigację. Wyłącznie polaczona-2/; bez git commit i git push.

## „Do potwierdzenia”
- Zachowano pięć już oznaczonych konfliktów: godziny POZ/gabinetu 8:00 kontra 7:30; Jarosław Kasperczak pon./czw. kontra pon./pt.; Julia Dobosz kontra Wiktoria Szczęsna; masaż 880 683 065 kontra 500 308 305; kalendarz szczepień 2025 kontra 2026. Nie znaleziono dodatkowego nieoznaczonego konfliktu z tabeli dla tej wersji.
- Uzupełniono uwagę o aktualności TPK i danych pomocy nocnej; dodano uwagę o dostępności, skierowaniu, terminach i finansowaniu badań na opisanym sprzęcie.
- Przy e-recepcie pozostawiono do potwierdzenia czas realizacji i możliwość odbioru w wybranym terminie. Opublikowanych wymagań formularza i sposobu przekazania kodu nie przedstawiono już jako nieznanych. Pozostałe wcześniejsze uwagi o brakach informacji zachowano.

## Weryfikacja i niewykonane
- PASS: python3 polaczona-2/build.py; kontrola 6 stron i 128 lokalnych linków/kotwic/zasobów, oryginalnych zdjęć, noindex, braku formularzy i zewnętrznych zasobów; kontrast AA; 5/5 testów planu dnia; składnia JS; git diff --check; dodatkowa kontrola obecności wszystkich uzupełnionych faktów.
- Poprawki treści z FACTCHECK odnoszące się do polaczona-2 wykonano. Nie sprawdzano wizualnie w przeglądarce ani nie potwierdzano telefonicznie aktualności danych. Podstawą są wskazane w briefie pliki audytu; rozbieżności wymagają rozstrzygnięcia przez przychodnię.
