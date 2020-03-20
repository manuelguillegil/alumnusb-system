import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnusb_system.settings")

import django
django.setup()

from django.core.files import File
from accounts.models import *

Profile_Picture.objects.all().delete()

img1 = Profile_Picture()

img1.Picture.save('img1.png', File(open('static/img/profile-pic/1.png', 'rb')))

img2 = Profile_Picture()

img2.Picture.save('img2.png', File(open('static/img/profile-pic/2.png', 'rb')))

img3 = Profile_Picture()

img3.Picture.save('img3.png', File(open('static/img/profile-pic/3.png', 'rb')))

img4 = Profile_Picture()

img4.Picture.save('img4.png', File(open('static/img/profile-pic/4.png', 'rb')))

img5 = Profile_Picture()

img5.Picture.save('img5.png', File(open('static/img/profile-pic/5.png', 'rb')))

img6 = Profile_Picture()

img6.Picture.save('img6.png', File(open('static/img/profile-pic/6.png', 'rb')))