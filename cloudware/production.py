from pickle import FALSE
from .settings import *

ALLOWED_HOSTS = ['cloudwaremx.herokuapp.com']

DEBUG = FALSE

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'