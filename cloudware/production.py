from pickle import FALSE
from .settings import *

ALLOWED_HOSTS = ['cloudwaremx.herokuapp.com']

DEBUG = FALSE

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'