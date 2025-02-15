
# Book Lending Library Application

A simple book lending library application built using Django and SQLite. This app allows users to manage books, track borrowing history, and record book returns.

# Features

✔️ CRUD operations for books (Create, Read, Update, Delete)

✔️ Track borrowing history of books

✔️ Borrow and return books while updating availability status

✔️ Basic data validations for integrity

✔️ Django’s built-in admin panel support

✔️ Includes unit tests for models

# Installation
Clone the repository
```bash
  git clone <repository-url> 
  cd book_lending
```
Setup Virtual environment

```bash
  python -m venv venv
  source venv/bin/activate #
```
   On Windows:
   ```bash
    venv\Scripts\activate
```
Install dependencies
```bash
  pip install -r requirements.txt 
```
Apply database migrations
```bash
 python manage.py migrate
```
Run development server
```bash
python manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/
    
