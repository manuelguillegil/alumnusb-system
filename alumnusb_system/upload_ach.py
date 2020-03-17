import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnusb_system.settings")

import django
django.setup()

from django.core.files import File
from accounts.models import *

Achievements.objects.all().delete()

ach1 = Achievements(Name='Numero donaciones bronce',
					Description='Llega a 5 donaciones')
ach1.Picture.save('nro_don_bronce.png', File(open('static/achiev_img/nro_don_bronce.png', 'rb')))

ach2 = Achievements(Name='Numero donaciones plata',
					Description='Llega a 10 donaciones')
ach2.Picture.save('nro_don_plata.png', File(open('static/achiev_img/nro_don_plata.png', 'rb')))

ach3 = Achievements(Name='Numero donaciones oro',
					Description='Llega a 20 donaciones')
ach3.Picture.save('nro_don_oro.png', File(open('static/achiev_img/nro_don_oro.png', 'rb')))

ach4 = Achievements(Name='Numero donaciones platino',
					Description='Llega a 30 donaciones')
ach4.Picture.save('nro_don_platino.png', File(open('static/achiev_img/nro_don_platino.png', 'rb')))

ach5 = Achievements(Name='Numero donaciones diamante',
					Description='Llega a 50 donaciones')
ach5.Picture.save('nro_don_diamante.png', File(open('static/achiev_img/nro_don_diamante.png', 'rb')))



ach6 = Achievements(Name='Total donaciones bronce',
					Description='Dona al menos 50 dolares')
ach6.Picture.save('total_don_bronce.png', File(open('static/achiev_img/total_don_bronce.png', 'rb')))

ach7 = Achievements(Name='Total donaciones plata',
					Description='Dona al menos 100 dolares')
ach7.Picture.save('total_don_plata.png', File(open('static/achiev_img/total_don_plata.png', 'rb')))

ach8 = Achievements(Name='Total donaciones oro',
					Description='Dona al menos 500 dolares')
ach8.Picture.save('total_don_oro.png', File(open('static/achiev_img/total_don_oro.png', 'rb')))

ach9 = Achievements(Name='Total donaciones platino',
					Description='Dona al menos 1000 dolares')
ach9.Picture.save('total_don_platino.png', File(open('static/achiev_img/total_don_platino.png', 'rb')))

ach10 = Achievements(Name='Total donaciones diamante',
					Description='Dona al menos 5000 dolares')
ach10.Picture.save('total_don_diamante.png', File(open('static/achiev_img/total_don_diamante.png', 'rb')))


ach11 = Achievements(Name='Donacion estrella bronce',
					Description='Realiza una donacion de al menos 100 dolares')
ach11.Picture.save('max_don_bronce.png', File(open('static/achiev_img/max_don_bronce.png', 'rb')))

ach12 = Achievements(Name='Donacion estrella plata',
					Description='Realiza una donacion de al menos 200 dolares')
ach12.Picture.save('max_don_plata.png', File(open('static/achiev_img/max_don_plata.png', 'rb')))

ach13 = Achievements(Name='Donacion estrella oro',
					Description='Realiza una donacion de al menos 300 dolares')
ach13.Picture.save('max_don_oro.png', File(open('static/achiev_img/max_don_oro.png', 'rb')))

ach14 = Achievements(Name='Donacion estrella platino',
					Description='Realiza una donacion de al menos 500 dolares')
ach14.Picture.save('max_don_platino.png', File(open('static/achiev_img/max_don_platino.png', 'rb')))

ach15 = Achievements(Name='Donacion estrella diamante',
					Description='Realiza una donacion de al menos 1000 dolares')
ach15.Picture.save('max_don_diamante.png', File(open('static/achiev_img/max_don_diamante.png', 'rb')))

ach16 = Achievements(Name='Donante',
					Description='Realiza una donacion')
ach16.Picture.save('donante.png', File(open('static/achiev_img/donante.png', 'rb')))

ach15 = Achievements(Name='Donante recurrente',
					Description='Realiza una donacion de al menos 1000 dolares')
ach15.Picture.save('recurrente.png', File(open('static/achiev_img/recurrente.png', 'rb')))

