"""
Django settings for avanzando project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k)axedfmqkx8ubgz_9d&059mfqbqo%o-c6e2vdixy)s*dktca3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'material',
    'material.admin',
    #'django_admin_bootstrapped',
    #'grappelli',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clients',
    'products',
    'product_categories',
    'sales',
    'tickets',
    'payments',
    'payment_methods',
        
)

# #suits
# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

# SUIT_CONFIG = {
#     'ADMIN_NAME': 'Avanzando Juntos',

#     'MENU':(
#         {'app': 'clients', 'label': 'Clientes', 'icon':'icon-lock'},
#         {'app': 'products', 'label': 'Productos', 'icon':'icon-home'},
#         )
#    }

#grapelli
# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.core.context_processors.request",
# )


        



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'avanzando.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'avanzando.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = "/Volumes/DATOS/Avanzando_Juntos/Avanzando/avanzando/static/"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Avanzando',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Backup settings

# DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
# DBBACKUP_TOKENS_FILEPATH = '/usr/local/tokens/'
# DBBACKUP_DROPBOX_APP_KEY = 'rdh2z7zclv4guju'
# DBBACKUP_DROPBOX_APP_SECRET = 'pfiw4twglnwwlh9'
