import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnusb_system.settings")

import django
django.setup()

from django.core.files import File
from accounts.models import *

Message.objects.all().delete()

msg1 = Message(Page='Resumen',
			   Title='Titulo mensaje pagina resumen',
			   Txt='Poner algun mensaje en el admin o en el script')

msg1.save()