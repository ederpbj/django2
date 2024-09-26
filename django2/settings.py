"""
Django settings for django2 project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from django.conf.global_settings import DATABASES

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
#DATABASE_URL = ' postgres://uejlalvfc198to:p81c6007db9ec89ceb3487b3c0cd228ff1b70b36746e1a1c524c2e1b9e37357bf@ccba8a0vn4fb2p.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dd5pnggais0hha'

# Usando postgresql com heroku
if os.getenv('DATABASE_URL'):
    # Configuração de banco de dados para Heroku
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    # Configuração de banco de dados local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'django2db',
            'USER': 'postgres',
            'PASSWORD': '098098Pg#',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }





# Substitua a configuração de DATABASES quando estiver no Heroku
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


#from django.conf.global_settings import EMAIL_BACKEND, MEDIA_URL, MEDIA_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-(p&4zusfz&p!a-)lw$tmzml(rvez7q&o#pjv0_m*_wl^j=yrve"

# Configurações de segurança
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-(p&4zusfz&p!a-)lw$tmzml(rvez7q&o#pjv0_m*_wl^j=yrve')


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "core",
    "bootstrap4",
    "stdimage",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql", # postgresql@14
        "NAME": "django2db",
        "USER": "postgres",
        "PASSWORD": "098098Pg#",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django2db",
        "USER": "root",
        "PASSWORD": "098098My#",
        "HOST": "localhost",
        "PORT": "",
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

#STATIC_URL = 'static/' # usado durante o desenvolvimento
STATIC_ROOT = BASE_DIR/'staticfiles' # usado durante a produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# serve para upload de arquivo
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGOUT_REDIRECT_URL = 'index'

# simula serviço envio de email
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# se ouver servidor de e-mail
"""
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'no-reply@seudominio.com.br'
EMAIL PORT = 587
EMAIL_USER_TSL = True
EMAIL_HOST_PASSWORD = 'sua-senha'
"""