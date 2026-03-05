## Autor

Projekt został wykonany przez Marta D.

Cyfrowa Biblioteka – Django MVC
Spis treści

Opis projektu

Funkcjonalności

Technologie

Instalacja i uruchomienie

Struktura projektu

1. Opis projektu

Projekt przedstawia prostą aplikację internetową stworzoną w frameworku Django z wykorzystaniem wzorca architektonicznego MVC (Model–View–Controller).

Aplikacja umożliwia zarządzanie kolekcją książek w cyfrowej bibliotece.

Użytkownik może:

przeglądać listę książek

dodawać nowe książki

edytować istniejące książki

usuwać książki

wyszukiwać książki w bazie

wypożyczać książki

oddawać książki

sprawdzać status książki (dostępna / wypożyczona)

Projekt został wykonany w ramach laboratorium dotyczącego wykorzystania wzorca MVC w aplikacjach internetowych.

2. Funkcjonalności

Aplikacja umożliwia:

wyświetlanie listy książek

dodawanie nowych książek

edycję książek

usuwanie książek (z potwierdzeniem)

wyszukiwanie książek

wyświetlanie statusu książki (dostępna / wypożyczona)

wypożyczanie książek użytkownikom

oddawanie książek

Modele w projekcie

Author – autor książki

Book – książka w bibliotece

Person – osoba wypożyczająca książkę

Borrowing – informacja o wypożyczeniu książki

Relacje między modelami

jedna książka posiada jednego autora

książka może mieć wiele wypożyczeń

jedno wypożyczenie jest powiązane z jedną osobą

3. Technologie

Projekt został wykonany przy użyciu:

Python 3.13

Django 6.0

SQLite

HTML

CSS

Git

GitHub

4. Instalacja i uruchomienie

Sklonuj repozytorium
git clone https://github.com/Martamm13/MVCLab1/tree/main/Project

Przejdź do folderu projektu
cd MVCLab1/Project

Zainstaluj Django
pip install django

Wykonaj migracje bazy danych
python manage.py migrate

Uruchom serwer
python manage.py runserver

Otwórz aplikację w przeglądarce
http://127.0.0.1:8000/library/

Panel administratora:
http://127.0.0.1:8000/admin/

5. Struktura projektu

Project/
│
├── library/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
│ └── library/
│ ├── index.html
│ ├── add_book.html
│ ├── edit_book.html
│ ├── delete_book.html
│ └── borrow_book.html
│
├── mysite/
│
└── manage.py

Projekt wykonany w ramach laboratorium MVC przez Marta D.