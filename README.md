StickyNotes Application - Part 2
--------------------------------
This is a Django-based sticky notes application (skeleton) with a modern look.
It includes:
- Django project skeleton and app 'stickynotes_app'
- Models, views, templates, static CSS (modern minimal theme)
- MariaDB-compatible settings (configure DB credentials in settings.py)
- Documentation compiled as PDF in /docs/documentation.pdf

To run (local dev):
1. Create a virtualenv and install requirements: pip install -r requirements.txt
2. Configure MariaDB and update DATABASES in stickynotes_project/settings.py
3. Run migrations: python manage.py makemigrations && python manage.py migrate
4. Create superuser: python manage.py createsuperuser
5. Run server: python manage.py runserver
