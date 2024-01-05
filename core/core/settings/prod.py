from .base import *

SECRET_KEY = 'django-insecure-b9&bs0n1-kx%ops6m(61!6y0m-a@w55(rm2tk76cxnga7vp@s3'
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
