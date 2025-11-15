# Stickynotes Project (Part 1 + 2 merged)

This project is prepared for HyperionDev coursework by **Mpho Kgooa**.

## Overview
Simple Django app that allows creating, editing, viewing and deleting notes.

## Setup (use a virtual environment)
1. Create and activate venv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MariaDB (optional - useful for HyperionDev evaluation):
   - Create a database and user in MariaDB.
   - Export environment variables before running migrations:
     ```bash
     export DB_ENGINE=django.db.backends.mysql
     export DB_NAME=stickynotes_db
     export DB_USER=your_db_user
     export DB_PASSWORD=your_db_password
     export DB_HOST=localhost
     export DB_PORT=3306
     ```
   If you don't set these, the project will use a local SQLite DB (db.sqlite3).
4. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Tests
Run tests with:
```bash
python manage.py test
```

## Diagrams
See the /diagrams folder for UML diagrams (class, use-case). These are included for the submission.
