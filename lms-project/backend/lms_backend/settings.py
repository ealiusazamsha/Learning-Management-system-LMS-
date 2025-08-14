"""Minimal Django settings placeholder."""

SECRET_KEY = 'replace-me'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

ROOT_URLCONF = 'lms_backend.urls'

WSGI_APPLICATION = 'lms_backend.wsgi.application'
