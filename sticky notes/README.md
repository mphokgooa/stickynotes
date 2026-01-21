# StickyNotes Project

This is a minimal, ready-to-upload Django project for the StickyNotes assignment.

## Quick start (development)

1. Create and activate virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Set environment variables (create a `.env` file or export env vars):
   ```
   SECRET_KEY='replace-this-with-a-secure-key'
   DJANGO_DEBUG=1
   DB_NAME=stickynotes_db
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

3. Run migrations and start:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Notes
- Database is configured for MariaDB/MySQL (django `mysqlclient`). If you prefer SQLite for testing, modify `settings.py` DATABASES accordingly.
- UML diagrams included: `uml/stickynotes_class.drawio` and `uml/stickynotes_class.png`.