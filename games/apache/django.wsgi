import os, sys
sys.path.append('/usr/local/django/gameswebsite')
sys.path.append('/usr/local/django/gameswebsite/games')
os.environ['DJANGO_SETTINGS_MODULE'] = 'games.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
