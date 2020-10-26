import os
from .base import *


SECRET_KEY = 'uj=pp7dz@a51rcpl9qw(!v0$#e&oe6%v53l8q1&6%2g%(@im@d'

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

