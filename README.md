# Django To-Do List with Authentication

This is a Django project that implements a to-do list application with user authentication. Users can create, manage, and track tasks, as well as sign up, log in, and manage their accounts.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Task Management**: Create, read, update, and delete tasks.
- **User-Specific Data**: Tasks are managed per user account.

## Requirements

- Python 3.x
- Django 5.x
- PostgreSQL (or other database, adjust settings accordingly)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-todo-app.git
   cd django-todo-app

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   
3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory of the project with the following content:
   
   ```bash
   DATABASE_NAME=todolist
   DATABASE_USER=postgres
   DATABASE_PASSWORD=0000
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   
  Note: Make sure to create the database named todolist in PostgreSQL before running migrations.

5. **Create Migrations:**

   ```bash
    python manage.py makemigrations

6. **Apply Database Migrations:**

    ```bash
    python manage.py migrate

7. **Run the Development Server:**

    ```bash
    python manage.py runserver
    
8. **Visit the Application:**
    Open http://127.0.0.1:8000/ in your web browser to use the application.
