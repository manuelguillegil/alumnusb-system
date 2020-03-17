from django.db import models
from django.contrib.auth.models import User
from accounts.utils import CountryField
from accounts.utils import CampusChoice
from accounts.utils import UndergraduateDegreeChoice

class User_information(models.Model):
	First_name = models.CharField(max_length=30, default='-')
	Middle_name = models.CharField(max_length=30, default='-')
	Last_name = models.CharField(max_length=30, default='-')
	Mailing_city = models.CharField(max_length=30, default='-')
	Mailing_state = models.CharField(max_length=30, default='-')
	USB_alumn = models.BooleanField(default=False)
	Codigo_Alumn_USB = models.CharField(max_length=30, default='-')
	Mailing_country = CountryField()
	Email = models.EmailField(max_length=60, unique=True)
	Mobile = models.CharField(max_length=30, default='-')
	Cohorte = models.IntegerField(default=0)
	Birthdate = models.DateField()
	Age = models.IntegerField(default=0)
	Undergrad_degree = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in UndergraduateDegreeChoice])
	Graduate_degree = models.CharField(max_length=60)
	Carnet = models.IntegerField(default=0)
	USB_undergrad_campus = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in CampusChoice])
	Graduate_campus = models.CharField(max_length=30, default='-')
	Work_email = models.EmailField(max_length=60)
	Workplace = models.CharField(max_length=30, default='-')
	Donor = models.BooleanField(default=False)
	Social_networks = models.CharField(max_length=50, default='-')
	Twitter_account = models.CharField(max_length=60,default='-')
	Instagram_account = models.CharField(max_length=60, default='-')

	def __str__(self):
		return self.Email

class User_stats(models.Model):
	Email = models.EmailField(max_length=60, unique=True)
	Average_gift = models.FloatField()
	Largest_gift = models.FloatField()
	Smallest_gift = models.FloatField()
	Total_gifts = models.FloatField()
	Best_gift_year_total = models.FloatField()
	Best_gift_year = models.IntegerField(null=True)
	First_gift_date = models.DateField(null=True)
	Last_gift_date = models.DateField(null=True)
	Total_number_of_gifts = models.IntegerField()

	def __str__(self):
		return self.Email

class Achievements(models.Model):
	Name = models.CharField(primary_key=True, max_length=50)
	Description = models.CharField(max_length=200)
	Picture = models.ImageField(default='static/achiev_img/C.png', upload_to='static/achiev_img/') 

	

class User_Achievements(models.Model):
	Owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	Achievement = models.ForeignKey(Achievements,on_delete=models.CASCADE,default=None)
	Date = models.DateField(auto_now_add=True)

	# Falta definir un __str__