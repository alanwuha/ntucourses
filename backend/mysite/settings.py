"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
import google.auth
from google.cloud import secretmanager_v1beta1 as sm
import logging

# Import settings with django-environ
env = environ.Env()

# Import settings from Secret Manager
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR,  ".env")

if not os.path.isfile('.env'):
    _, project = google.auth.default()
    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, "django-settings", "1")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")

        with open(env_file, "w") as f:
            f.write(payload)

env.read_env(env_file)

# Pull values from environment
DATABASE_HOST = env('DATABASE_HOST')
DATABASE_NAME = env('DATABASE_NAME')
DATABASE_USER = env('DATABASE_USER')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DEBUG = int(env('DEBUG'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%!1=z!afk8+4&qxv!2*hp15-f_h_j9v*02$w6cy3pu!+w&z99g'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'scraping',
    'api',
    'corsheaders',
    'elasticapm.contrib.django'
]

ELASTIC_APM = {
  # Set required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'ntucourses',

  # Use if APM Server requires a token
  'SECRET_TOKEN': 'lNAoZdzpIFTCW52QBi',

  # Set custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'https://74e49c406bc94717bc4fa9571e294283.apm.asia-southeast1.gcp.elastic-cloud.com:443',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'elasticapm.contrib.django.middleware.TracingMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.getenv('GAE_APPLICATION', None):
    # Running on App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': DATABASE_HOST,
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
        }
    }
else:
    # Running locally so connect to either a local PostgreSQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:5432
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': DATABASE_HOST,
            'PORT': '5432',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Django Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    # User Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticed users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}

CORS_ORIGIN_ALLOW_ALL = True