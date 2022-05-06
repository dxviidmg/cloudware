from .settings import *

ALLOWED_HOSTS = ['cloudwaremx.herokuapp.com']

import dj_database_url
DATABASES = {'default': dj_database_url.config()}