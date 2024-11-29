"""
Django settings for ChatClassRoom project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)r1dkxcc89u_@-&&7g-!_2!b_0#rfs7%7p$-qy1-v&)^6e_-4p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Django's built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'crispy_tailwind',
    'widget_tweaks',
    'compressor',

    # Your apps
    'main.apps.MainConfig',
    'rest_framework',

    # PWA
    'pwa',
    
    # Third-party apps
    'django.contrib.sites',  # Required for allauth
    'allauth',               # Core allauth app
    'allauth.account',       # Allauth account management
    'allauth.socialaccount', # Allauth social login support

    # Add any specific providers you're using
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
]

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Required for allauth
]

SITE_ID = 1

# Redirect URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Email verification settings
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Options: 'mandatory', 'optional', 'none'
ACCOUNT_EMAIL_REQUIRED = True

# Signup/registration settings
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # Options: 'username', 'email', 'username_email'

# Other settings
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'ChatClassRoom.urls'

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

# WSGI_APPLICATION = 'ChatClassRoom.wsgi.application'
WSGI_APPLICATION = 'ChatClassRoom.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Add these at the top of your settings.py
from os import getenv

# Replace the DATABASES section of your settings.py with this
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',       # Using PostgreSQL as the database engine
#         'NAME': 'postgres',                              # The database name
#         'USER': 'postgres.ycdhugtadteuliqkrjxw',         # The database user
#         'PASSWORD': 'Siddharth@6307862150',              # The password (replace [YOUR-PASSWORD] with the actual password)
#         'HOST': 'aws-0-ap-south-1.pooler.supabase.com',  # The host
#         'PORT': '6543',                                  # The port number
#         'CONN_MAX_AGE': 600,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# URL to use when referring to static files (where they will be served from)
STATIC_URL = 'static/'

# The directory where collectstatic will collect static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional locations of static files (do not include STATIC_ROOT here)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # This is the project-wide static directory
]

# Make sure the STATICFILES_FINDERS settings are configured correctly as well:
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary settings

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = "durdi1oak",
    api_key = "164254991127435",
    api_secret = "i8Lzr2SSRJCAlHS_6l0NVqrDkc4",
    api_proxy = "http://proxy.server:3128"
)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'durdi1oak',
    'API_KEY': '164254991127435',
    'API_SECRET': 'i8Lzr2SSRJCAlHS_6l0NVqrDkc4',
}

# Use Cloudinary as the storage backend for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Media files
MEDIA_URL = '/media/'  # Set the media URL to a path in your Django project
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Set the local media root folder

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'llsiddharthtiwarill@gmail.com'
EMAIL_HOST_PASSWORD = 'font qeui toiz shjl'


# PWA settings

PWA_APP_NAME = 'ChatClassRoom'
PWA_APP_DESCRIPTION = 'Where knowledge meets fun, and boredom takes a backseat. Dive in, explore, and let\'s make learning awesome!'
PWA_APP_THEME_COLOR = '#FFFFFF'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/images/logo.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/logo.png',
        'sizes': '512x512'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
