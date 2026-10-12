# Raport zmian — 13 października 2026

## Co zmieniono

- Początek strony prowadzi przez pięć zadań: godziny, grafik zespołu, laboratorium, szczepienia, informacje dla pacjenta. Każde ma widoczny skrót na początku strony.
- Przyklejony nagłówek pokazuje telefon rejestracji POZ: **62 580 22 52**. Pierwszy blok pokazuje dzisiejszy plan POZ według dnia tygodnia w strefie Europe/Warsaw, z uwagą o świętach i konieczności potwierdzenia godzin.
- Zachowano typografię, czerwony akcent #b01f2c, komponenty i przełącznik wyglądu. Dodano istniejącą medyczną zieleń #277049 do informacji o godzinach; tło jest białe. „O nas”, programy i informacje prawne są niżej.
- Przywrócono szczegóły piątkowych grafików z oferty POZ. Specjaliści są rozwijaną częścią grafiku. Telefon dietetyka poprawiono na źródłowy **791 755 792**. Wszystkie numery są linkami tel:.
- E-recepta jest wyraźnie oznaczonym podglądem bez formularza zbierającego dane. Dojazd prowadzi do mapy przez link; podgląd nie pobiera zewnętrznych kafelków. Dodano odnośnik do źródłowego komunikatu o naruszeniu danych MyDr. Klawisze strzałek poza przełącznikiem wyglądu pozwalają przewijać stronę.

## Fakty oznaczone „do potwierdzenia”

1. **Godziny:** osobny grafik rejestracji POZ; POZ i gabinet zabiegowy 8:00–18:00 wobec 7:30–18:00 w stopce; piątek Pawła Andrzejczaka, dla którego źródło podaje 8:00–18:00 w dni nieparzyste.
2. **Zespół:** nazwiska i dyżury pielęgniarek oraz położnej; brakujące godziny Karoliny Tworek, Anety Kliber, Justyny Prus-Buczak i dietetyka; dni Jarosława Kasperczaka; nazwisko dietetyka (wybrano Julię Dobosz ze strony „O nas”, strona główna podaje Wiktorię Szczęsną); numer rejestracji na masaż (wybrano szczegółowy numer ze strony głównej).
3. **Laboratorium:** lista i wskazania badań, skierowanie, zakres NFZ i ceny; przygotowanie, w tym pozostawanie na czczo; miejsce i sposób odbioru wyników, dostęp online oraz termin po piątkowym pobraniu. Zachowano źródłowe pobrania pon–pt 7:30–11:00 i wyniki następnego dnia od 14:00.
4. **Szczepienia:** rok kalendarza (wybrano 2026 z treści wobec 2025 w tytule), aktualna dostępność, zakres szczepień skojarzonych, wiek, kwalifikacja, dawki i finansowanie.
5. **E-recepta:** sposób zamawiania i termin realizacji.

## Weryfikacja i rzeczy pozostawione

- Projekt jest statyczny: nie ma package.json ani polecenia build. Sprawdzono składnię JavaScript, poprawność zagnieżdżenia HTML, unikalność ID, jeden h1, noindex/nofollow oraz brak formularzy i zewnętrznych skryptów/fontów.
- Kontrola wykazała **0 błędnych lokalnych odnośników**: sprawdzono 36 odwołań HTML i 66 odwołań CSS do zasobów. Wszystkie 14 numerów telefonu występuje w audycie. Testy wykonywania JS potwierdziły dzień roboczy, weekend, granice daty w Warszawie i obsługę klawiatury przełącznika. Nie wykazały wyjątków w testowanych ścieżkach.
- Kontrast podstawowych kolorów wynosi co najmniej 5,17:1. Kontrola git diff --check przechodzi. Skan projektu wykazał odziedziczone ozdobniki wariantów; zachowano je zgodnie z poleceniem utrzymania charakteru. Powiększono drobne etykiety i obszary dotykowe.
- **Pozostało sprawdzenie wizualne na 360/390 px oraz konsola rzeczywistej przeglądarki.** Narzędzie Playwright wymaga niedostępnej zgody, Chrome nie uruchamia się w sandboxie, a przeglądarka Chrome nie jest dostępna w narzędziu UI. Nie potwierdzono pomiarami braku poziomego przepełnienia ani reguły 3 sekund. Zewnętrznych odnośników nie sprawdzono przez HTTP. Blok „Dziś” pokazuje zwykły grafik tygodniowy, nie wykrywa świąt; uwaga jest widoczna obok godzin. Brakujących danych i szczegółowego kalendarza szczepień nie dopisano bez źródeł.
- Zmieniono wyłącznie pliki w klasyczne/. Nie wykonano git commit ani git push. Istniejącej wcześniej zmiany w pytania/index.html nie dotykano.

## Przegląd uwag hooka

- Trzy zgłoszenia bocznych akcentów dotyczą odziedziczonych elementów: informacji pomocniczych, faktów przy e-recepcie i kart programów NFZ. Zachowano je zgodnie z zakresem „re-layout, nie nowy design”.
- Zgłoszenie zbyt małego odstępu w bloku faktów e-recepty jest fałszywym alarmem: CSS zapewnia co najmniej 19,2 px odsunięcia tekstu od boków, a pozostałe warianty mają 20 px.
- Zapisano wyjątki tylko dla tych dwóch reguł i index.html w klasyczne/.impeccable/config.json. Nie wyłączono żadnej reguły dla całego projektu. Nie zmieniano wyglądu w odpowiedzi na te uwagi.
- Po zastosowaniu wyjątków skan uruchomiony z klasyczne/ nie zgłasza problemów wymagających poprawy; pozostawia dwie uwagi informacyjne o odziedziczonym tle dojazdu i interpunkcji.
