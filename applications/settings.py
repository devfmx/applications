"""Dev.f Applications settings file."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ENVIRONMENT = os.getenv('ENVIRONMENT')
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    'aplica.devf.mx'
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

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

ROOT_URLCONF = 'applications.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'applications.wsgi.application'

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('PRODUCTION_DATABASE_NAME'),
            'USER': os.getenv('PRODUCTION_DATABASE_USER'),
            'PASSWORD': os.getenv('PRODUCTION_DATABASE_PASSWORD'),
            'HOST': os.getenv('PRODUCTION_DATABASE_HOST'),
            'PORT': os.getenv('PRODUCTION_DATABASE_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DEVELOPMENT_DATABASE_NAME'),
            'USER': os.getenv('DEVELOPMENT_DATABASE_USER'),
            'PASSWORD': os.getenv('DEVELOPMENT_DATABASE_PASSWORD'),
            'HOST': os.getenv('DEVELOPMENT_DATABASE_HOST'),
            'PORT': os.getenv('DEVELOPMENT_DATABASE_PORT'),
        }
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
