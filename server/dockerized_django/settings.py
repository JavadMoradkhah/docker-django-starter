import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(key, default=None):
    value = os.getenv(key, default) if default is not None else os.getenv(key)

    if os.path.isfile(value):
        with open(value) as f:
            return f.read()

    return value


def split_env(var_name, separator, default):
    value = os.environ.get(var_name)
    return value.split(separator) if value is not None else default


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a comma between each.
# For example: DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
ALLOWED_HOSTS = split_env("DJANGO_ALLOWED_HOSTS", ',', [])

# 'DJANGO_CSRF_TRUSTED_ORIGINS' should be a single string of hosts with a comma between each.
# For example: DJANGO_CSRF_TRUSTED_ORIGINS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS = split_env("DJANGO_CSRF_TRUSTED_ORIGINS", ',', [])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dockerized_django.urls'

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

WSGI_APPLICATION = 'dockerized_django.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER', 'postgres'),
        "HOST": os.environ.get('DB_HOST', '127.0.0.1'),
        "PORT": os.environ.get('DB_PORT', '5432'),
        "PASSWORD": get_secret('DB_PASSWORD_FILE')
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "mediafiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
