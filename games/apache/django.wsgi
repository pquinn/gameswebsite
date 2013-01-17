import os, sys

activate_this = os.path.join('/usr/local/django/gameswebsite/venv', 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

root_path = '/usr/local/django/gameswebsite'
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, 'games'))
sys.path.append('/usr/local/django/gameswebsite/venv/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'games.apache.settings_production'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()