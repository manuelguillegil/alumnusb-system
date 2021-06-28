import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnusb_system.settings")

import django
django.setup()

from django.core.files import File
from accounts.models import *

Achievements.objects.all().delete()

ach1 = Achievements(Name='Numero donaciones bronce',
					Description='Llega a 5 donaciones',
					Level=1)
ach1.Picture.save('nro_don_bronce.png', File(open('static/img/medals/t2-1.png', 'rb')))

ach2 = Achievements(Name='Numero donaciones plata',
					Description='Llega a 10 donaciones',
					Level=2)
ach2.Picture.save('nro_don_plata.png', File(open('static/img/medals/t2-2.png', 'rb')))

ach3 = Achievements(Name='Numero donaciones oro',
					Description='Llega a 20 donaciones',
					Level=3)
ach3.Picture.save('nro_don_oro.png', File(open('static/img/medals/t2-3.png', 'rb')))

ach4 = Achievements(Name='Numero donaciones platino',
					Description='Llega a 50 donaciones',
					Level=4)
ach4.Picture.save('nro_don_platino.png', File(open('static/img/medals/t2-4.png', 'rb')))

ach5 = Achievements(Name='Numero donaciones diamante',
					Description='Llega a 100 donaciones',
					Level=5)
ach5.Picture.save('nro_don_diamante.png', File(open('static/img/medals/t2-6.png', 'rb')))



ach6 = Achievements(Name='Total donaciones bronce',
					Description='Dona al menos 100 dolares',
					Level=1)
ach6.Picture.save('total_don_bronce.png', File(open('static/img/medals/t1-1.png', 'rb')))

ach7 = Achievements(Name='Total donaciones plata',
					Description='Dona al menos 500 dolares',
					Level=2)
ach7.Picture.save('total_don_plata.png', File(open('static/img/medals/t1-3.png', 'rb')))

ach8 = Achievements(Name='Total donaciones oro',
					Description='Dona al menos 1500 dolares',
					Level=3)
ach8.Picture.save('total_don_oro.png', File(open('static/img/medals/t1-5.png', 'rb')))

ach9 = Achievements(Name='Total donaciones platino',
					Description='Dona al menos 3000 dolares',
					Level=4)
ach9.Picture.save('total_don_platino.png', File(open('static/img/medals/t1-7.png', 'rb')))

ach10 = Achievements(Name='Total donaciones diamante',
					Description='Dona al menos 5000 dolares',
					Level=5)
ach10.Picture.save('total_don_diamante.png', File(open('static/img/medals/t1-8.png', 'rb')))


ach11 = Achievements(Name='Donacion estrella bronce',
					Description='Realiza una donacion de al menos 5 dolares',
					Level=1)
ach11.Picture.save('max_don_bronce.png', File(open('static/img/medals/t3-1.png', 'rb')))

ach12 = Achievements(Name='Donacion estrella plata',
					Description='Realiza una donacion de al menos 20 dolares',
					Level=2)
ach12.Picture.save('max_don_plata.png', File(open('static/img/medals/t3-2.png', 'rb')))

ach13 = Achievements(Name='Donacion estrella oro',
					Description='Realiza una donacion de al menos 50 dolares',
					Level=3)
ach13.Picture.save('max_don_oro.png', File(open('static/img/medals/t3-3.png', 'rb')))

ach14 = Achievements(Name='Donacion estrella platino',
					Description='Realiza una donacion de al menos 100 dolares',
					Level=4)
ach14.Picture.save('max_don_platino.png', File(open('static/img/medals/t3-4.png', 'rb')))

ach15 = Achievements(Name='Donacion estrella diamante',
					Description='Realiza una donacion de al menos 500 dolares',
					Level=5)
ach15.Picture.save('max_don_diamante.png', File(open('static/img/medals/t3-5.png', 'rb')))

ach16 = Achievements(Name='Donante',
					Description='Realiza una donacion',
					Level=5)
ach16.Picture.save('donante.png', File(open('static/img/medals/t5.png', 'rb')))

ach17 = Achievements(Name='Donante recurrente',
					Description='Realiza una donacion de al menos 1000 dolares',
					Level=5)
ach17.Picture.save('recurrente.png', File(open('static/img/medals/t4.png', 'rb')))

