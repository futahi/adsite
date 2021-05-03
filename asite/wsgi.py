"""
WSGI config for asite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
import sys

# add your project directory to the sys.path
path = '/home/futahi/adsite/asite/'
if path not in sys.path:
    # sys.path.insert(0, path)
    sys.path.append(path)

os.chdir(path)

# set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'asite.settings')

# Import your Django project's configuration
import django
django.setup()

# Import the Django WSGI to handle any requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()