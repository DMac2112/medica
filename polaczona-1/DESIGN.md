# ARSMEDICA — Dziś w przychodni

Cel: pacjent 60+ na telefonie widzi godziny POZ i telefon bez przewijania; godziny, lekarze, badania i szczepienia są dostępne jednym dotknięciem. Podgląd, nie serwis produkcyjny. Źródła: brief overnight, audit/pages i AUDIT.md. Zapis projektu zastępuje dodatkową rundę wyboru: użytkownik wskazał już kierunek i polecił zbudować tę wersję.

## Pomysł i przegląd trzech wersji
Klasyczne: trwała czytelność, pełny tygodniowy grafik i rodzima nawigacja details. Centrum: krótka droga do pięciu spraw pacjenta, praktyczny układ usług. Next: osobne godziny usług, strefa Europe/Warsaw, uczciwe oznaczenia brakujących danych. Nowa kompozycja: tablica dnia, nie kolejna strona promocyjna.

## System
Czerwień #b3141f z Next, zieleń #385e4a, jasna zieleń #edf3ef, biel #ffffff, tekst #242c29, tekst pomocniczy #526259. Public Sans (lokalny, czytelny tekst) i Archivo 700 (lokalny, zwarta typografia tablicy), oba z polskimi znakami. Treść 18px lub więcej; pomocnicze uwagi 16px. Wyrównanie do lewej, duże cele 48px.

## Kompozycja
Telefon: marka + telefon / pięć skrótów / tablica dnia z godzinami / pobrania / dzisiejsi lekarze / szczepienia / kontakt. Desktop: wspólna duża tablica, po lewej godziny i pobrania, po prawej lista dyżurów na osi 8–18; niżej autentyczna rejestracja i informacje.

## Ryzyko
Duża czerwona tablica dnia przywołuje fizyczną informację z poczekalni. Czerwień ma tutaj funkcję orientacji, nie alarmu: brak migania, brak neonów i brak „żywych” wskaźników. Oś czasu pokazuje prawdziwe proporcje godzin. Reszta układu spokojna, biała, bez identycznych kafelków i hover-lift.

## Uczciwość
Status to wyłącznie plan obliczony z zegara urządzenia i grafiku, nie obecność personelu ani dostępność wizyt. Piątków parzystych/nieparzystych nie rozstrzygamy. Święta oznaczamy osobno; wyjątki i aktualność do potwierdzenia. Bez JS są pełne godziny tygodniowe i grafiki. Nie zbieramy danych. Zdjęcie oryginalne, hash sprawdzony z hub/image-sources.json.

## Sprawdzenie
Testy zegara, granic godzin, osobnego punktu pobrań, weekendów, świąt i niejasnych piątków; przegląd 360/390px i desktopu, bez JS, linki, noindex, focus, kontrast i brak zewnętrznych zasobów. Edycje wyłącznie polaczona-1/.
