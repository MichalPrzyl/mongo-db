# MongoDB Playground 🧪

To repozytorium zawiera pierwsze testy z bazą danych **MongoDB** przy użyciu języka **Python** i biblioteki `pymongo`.

## Co robię aktualnie

- Łączę się lokalnie z instancją MongoDB (domyślnie na `localhost:27017`)
- Tworzę dokumenty typu `{"hero": "Adam"}` i zapisuję je do kolekcji
- Wyszukuję dokumenty po polach (`find`, `find_one`)
- Eksperymentuję z podstawowymi operacjami typu `insert_one`, `update_one`, `delete_many`

## Co chcę zrealizować w kolejnych krokach

- Dodanie pól z datą (`created_dt`) i filtrowanie po czasie
- Testowanie struktur zagnieżdżonych i referencji (relacje użytkownik–produkty)
- Eksport danych do JSON-a i import z powrotem
- Testy indeksów i zapytań z operatorami (`$gt`, `$regex`, `$or`)
- Podpięcie lambdy z AWS do clustra mongoDB

##  Jak uruchomić

1. Upewnij się, że MongoDB działa lokalnie (`docker run -p 27017:27017 mongo`)
2. Zainstaluj zależności (ja to robiłem w `venv`):

```bash
pip install pymongo
```
