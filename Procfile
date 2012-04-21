web: python games/manage.py collectstatic --noinput; gunicorn_django --workers=4 --bind=0.0.0.0:$PORT games/settings.py
