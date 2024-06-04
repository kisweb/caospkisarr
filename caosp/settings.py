"""
Django settings for caosp project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://bold-surf-f3cccb0c.lz1mmz.on-acorn.io']

AUTH_USER_MODEL = 'account.User'

try:
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger'
    }
except Exception as e:
    pass    


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    
    "django_htmx",
    "template_partials",    
    "import_export",
    "crispy_forms",
    "crispy_bootstrap5",
    "formtools",
    "debug_toolbar",
    "account",
    "core",
    "etablissement",
    'quote',
    'anneescolaire',
    'django_extensions',
    'ninja',
    'corsheaders',
    'commande',
    'gestion',
]
# postgres://caosp:8C2oTGMEPY64a71oKqbYWvwCBsqZwoz5@dpg-cmganio21fec739ottig-a.frankfurt-postgres.render.com/quoteparts
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'login_required.middleware.LoginRequiredMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "caosp.urls"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8001",
    "https://caospzig.onrender.com/",
    
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": ['templates'],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
# Install app and configure loader.
default_loaders = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]
cached_loaders = [("django.template.loaders.cached.Loader", default_loaders)]
partial_loaders = [("template_partials.loader.Loader", cached_loaders)]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        # Comment this out when manually defining loaders.
        # "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": True,
            # TODO: Add wrap_loaded function to the called from an AppConfig.ready().
            "loaders": partial_loaders,
        },
    },
]

WSGI_APPLICATION = "caosp.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASE_URL=postgres://caosp:8C2oTGMEPY64a71oKqbYWvwCBsqZwoz5@dpg-cmganio21fec739ottig-a.frankfurt-postgres.render.com/quoteparts

DATABASES = {
    'default': dj_database_url.parse(config('postgres://caosp:8C2oTGMEPY64a71oKqbYWvwCBsqZwoz5@dpg-cmganio21fec739ottig-a.frankfurt-postgres.render.com/quoteparts'))
}

#DATABASES = {
#
#    'default': {
#
#       'ENGINE': 'django.db.backends.postgresql',
#      'NAME': 'caospkisarr',
#        'USER': 'kisarr',
#        'PASSWORD': 'kisarr',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

# PGPASSWORD=8C2oTGMEPY64a71oKqbYWvwCBsqZwoz5 psql -h dpg-cmganio21fec739ottig-a.frankfurt-postgres.render.com -U caosp quoteparts

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = False

ANNEES = (
("2023-2024", "2023-2024"),
("2024-2025", "2024-2025"),
("2025-2026", "2025-2026"),
("2026-2027", "2026-2027"),
("2027-2028", "2027-2028"),
("2028-2029", "2028-2029"),
("2029-2030", "2029-2030"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "account:login"

INTERNAL_IPS = [
    "127.0.0.1",
]
