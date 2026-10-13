# Raport: nowe wersje w hubie

- Dodano karty „Połączona 1” i „Połączona 2” w `index.html`, z krótkimi opisami i lokalnymi linkami do istniejących folderów.
- Zaktualizowano `hub/catalog.json`, choć obecny hub wyświetla karty bezpośrednio z HTML.
- Zachowano wygląd istniejących kart; w `hub/sites.css` dodano wariant bez zdjęcia, z opisem 18px i poprawnym układem ostatniej karty na tabletach.
- „Do potwierdzenia”: nie dodano nowych faktów medycznych ani nowych oznaczeń. Istniejące oznaczenia w obu wersjach pozostawiono bez zmian.
- Kontrole zakończone: zgodność wszystkich sześciu kart z katalogiem, nazwy i opisy, lokalne linki do obu nowych wersji, dostępność istniejących zdjęć, noindex/nofollow oraz `git diff --check`.
- Niewykonane: zrzuty podglądów i wizualna kontrola mobilna. Lokalny Chromium nie uruchamia się w sandboxie (`MachPortRendezvousServer: Permission denied`). Zgodnie z poleceniem użyto kart bez zdjęć.
- Nie edytowano obu wersji ani `pytania/`; istniejąca zmiana w `pytania/index.html` była obecna przed rozpoczęciem. Nie wykonano commit ani push.
