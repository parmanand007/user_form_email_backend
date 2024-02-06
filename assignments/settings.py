"""
Django settings for assignments project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#x^nw@gz6w9ndz2bmf3!a1af8_p2e8z-^7v)+johko6hn5=eg7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*",'.vercel.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'phonenumber_field',
    'simpleForm',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000','https://user-form-email-frontend.vercel.app'
]
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'assignments.urls'

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

WSGI_APPLICATION = 'assignments.wsgi.application'

# settings.py

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# postgresql://postgres:D35b4*bcg1GdB4fAb1E2F*gfBFe6dF6a@postgres.railway.internal:5432/railway
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "63f1D11dF6gaD*dA46C13bda4Ab-g3AF",
        "HOST": "viaduct.proxy.rlwy.net",
        "PORT": "37781",
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# # set the celery broker url 
# # CELERY_BROKER_URL = 'redis://default:nHE1ahhGMJiaeIaOIaKLi62GfeOdlfEI@viaduct.proxy.rlwy.net:55189'
  
# CELERY_BROKER_URL = 'redis://default:nHE1ahhGMJiaeIaOIaKLi62GfeOdlfEI@redis.railway.internal:6379'
# # set the celery result backend 
# # CELERY_RESULT_BACKEND = 'redis://default:nHE1ahhGMJiaeIaOIaKLi62GfeOdlfEI@viaduct.proxy.rlwy.net:55189'
# CELERY_RESULT_BACKEND = 'redis://default:nHE1ahhGMJiaeIaOIaKLi62GfeOdlfEI@redis.railway.internal:6379'
  
# # set the celery timezone 
# CELERY_ACCEPT_CONTENT=['application/json']
# CELERY_RESULT_SERIALIZER='json'
# CELERY_TASK_SERIALIZER='json'

# CELERY_TIMEZONE = "Asia/Kolkata"
# # CELERY_TASK_TRACK_STARTED = True
# # CELERY_TASK_TIME_LIMIT = 30 * 60
# broker_connection_retry_on_startup = True


REDIS_URL = 'redis://default:4B5jgDE2hFOfoPpPDOeJBfic2ANComeo@roundhouse.proxy.rlwy.net:46494'

AUTH_USER_MODEL ='simpleForm.User'
SENDER_EMAIL = 'parmanand.p@brimo.in'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD ='gmail app code'
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
