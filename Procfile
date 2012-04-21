web: python mysiteheroku/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT mysiteheroku/settings.py
