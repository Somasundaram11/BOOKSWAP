# BookSwap

BookSwap is a beginner-friendly full-stack web application built using Django, SQLite, and Bootstrap 5. It features a modern dark-themed user interface with custom CSS styles, card hover animations, and a blue/indigo gradient accent.

This application is designed to demonstrate standard **CRUD (Create, Read, Update, Delete)** operations, search filtering, and dashboard telemetry in a clean, production-ready Django project structure.

---

## Features

1. **Home Page**: A landing page with a hero banner, welcome text, and call-to-action buttons.
2. **Dashboard**: Live telemetry indicating the total number of books registered and a list of the 5 most recently added books.
3. **Book Directory (Read)**: View all listed books in a responsive card layout.
4. **Search Filter**: Search through listings by book title or author.
5. **Manage Listings (Create/Update/Delete)**: Add, edit details, and delete book entries with a confirmation page.

---

## Tech Stack
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Backend**: Django 6.0
- **Database**: SQLite3 (Default, lightweight database)

---

## Folder Structure

```text
bookswap/
│
├── books/                 # Django App for books catalog
│   ├── migrations/        # Database migrations
│   ├── admin.py           # Django Admin panel registration
│   ├── apps.py            # App configurations
│   ├── forms.py           # Dynamic ModelForm with Bootstrap classes
│   ├── models.py          # Book model definition
│   ├── tests.py           # Unit tests for CRUD and search
│   ├── urls.py            # App-level routing
│   └── views.py           # CRUD and dashboard views
│
├── bookswap/              # Project settings and core config
│   ├── settings.py        # Django settings (Template/Static config)
│   ├── urls.py            # Root URL routing
│   └── wsgi.py / asgi.py
│
├── templates/             # HTML Templates
│   ├── base.html          # Global page layout (navbar, footer, styling link)
│   ├── home.html          # Welcome hero landing page
│   ├── dashboard.html     # Telemetry counters and recent book tables
│   └── books/
│       ├── list.html      # Book list directory & search page
│       ├── add.html       # Add book form
│       ├── edit.html      # Edit book form
│       ├── detail.html    # Book details inspection page
│       └── delete.html    # Delete confirmation prompt
│
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Dark theme styling, gradients, and hover transitions
│   └── images/
│
├── manage.py              # Django CLI utility
└── db.sqlite3             # Local SQLite database file
```

---

## Installation & Setup

Follow these steps to set up and run the application locally:

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your machine.

### 2. Create and Activate a Virtual Environment
In the root directory of the project, create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate on Linux/macOS:
source venv/bin/activate

# Activate on Windows:
# venv\Scripts\activate
```

### 3. Install Django
Install Django inside the virtual environment:
```bash
pip install django
```

### 4. Apply Database Migrations
Create the SQLite database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
Create an administrator account to access the Django admin panel (`http://127.0.0.1:8000/admin/`):
```bash
python manage.py createsuperuser
```

### 6. Run the Application
Start the Django development server:
```bash
python manage.py runserver
```
Visit the application in your browser at `http://127.0.0.1:8000/`.

---

## Running Automated Tests
We have built unit tests covering all views, models, forms, and search functionality. You can run these tests using:
```bash
python manage.py test
```
