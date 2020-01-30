## Panel Admina
https://ar4py.herokuapp.com/admin/
Dane do zalogowania na konwersacji

## API
https://ar4py.herokuapp.com/api/ 
#### Wizyty:
https://ar4py.herokuapp.com/api/appointments/

| Metoda | Adres                   |  Opis                       |
| :----: |:-----------------------:| :--------------------------:|
| GET    | /api/appointments/      | Lista wszystkich wizyt      |
| POST   | /api/appointments/      | Utworzenie nowej wizyty     |
| GET    | /api/appointments/next/ | Pokazanie następnej wizyty  |

## Dokumentacja:
ar4py jest backendem projektu zespołowego. Backend jest oparty o framework django: https://docs.djangoproject.com/en/3.0/.
Backend służy do przechowywania informacji na temat zarejestrowanych użytkowników i ich wizyt. Baza danych obsługująca system to PostgreSQL: https://www.postgresql.org/docs/. API jest wystawiony w oparciu o framework Django REST Framework: https://www.django-rest-framework.org/

### Sposób działania:
Frontend za pomocą requestów AJAX wysyła zapytanie do API. API odbiera informacje na temat danych studenta oraz proponowanej godziny wizyty. Następnie jest obliczona najbliższa wolna godzina dla tego studenta. W bazie danych jest tworzona informacja o tej wizycie która następnie jest zwracana do Frontendu gdzie jest wyświetlana użytkowniko wraz z jego unikalnym numerem.
