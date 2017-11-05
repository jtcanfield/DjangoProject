To start:
django-admin.py startproject firstdjangoproject
cd /firstdjangoproject
./manage.py startapp core

changed second firstdjangoproject folder to settings
change name in manage.py line 6 to settings
change name in settings.py line 53 and 71 to settings
change name in wsgi.py line 14 to settings

in settings.py: added
INSTALLED_APPS = [
    'core',
]


in urls.py: added
from core.views import greeting_view
urlpatterns = [
    url(r'^$', greeting_view),
]


to start:
$ python manage.py runserver
