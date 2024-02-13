from .common import *
from .utils import split_env

DEBUG = False

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a comma between each.
# For example: DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
ALLOWED_HOSTS = split_env("DJANGO_ALLOWED_HOSTS", ',', [])

# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
# CSRF_COOKIE_SECURE = True

# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
# SESSION_COOKIE_SECURE = True

# 'DJANGO_CSRF_TRUSTED_ORIGINS' should be a single string of hosts with a comma between each.
# For example: DJANGO_CSRF_TRUSTED_ORIGINS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS = split_env("DJANGO_CSRF_TRUSTED_ORIGINS", ',', [])

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.Filehandler',
            'filename': BASE_DIR / 'app_logs.log'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', default='ERROR')
        }
    }
}