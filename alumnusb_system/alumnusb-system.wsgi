import os
import signal

import sys
import traceback

import time
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnusb_system.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)