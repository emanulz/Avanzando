import os, sys
sys.path.append('/Volumes/DATOS/Avanzando_Juntos/Avanzando/avanzando')
os.environ['DJANGO_SETTINGS_MODULE'] = 'avanzando.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()