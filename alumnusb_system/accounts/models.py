from django.db import models
from django.contrib.auth.models import User
from accounts.utils import CountryField
from accounts.utils import CampusChoice
from accounts.utils import UndergraduateDegreeChoice

# Model to upload the AlumnUSB fields to our database
class alumncsv(models.Model):
	Account_id = models.CharField(max_length=50,null=True,blank=True)
	First_name = models.CharField(max_length=400,null=True,blank=True)
	Middle_name = models.CharField(max_length=400,null=True,blank=True)
	Last_name = models.CharField(max_length=400,null=True,blank=True)
	Mailing_city = models.CharField(max_length=400,null=True,blank=True)
	Mailing_state = models.CharField(max_length=400,null=True,blank=True)
	USB_alumn = models.IntegerField(null=True,blank=True)
	Codigo_Alumn_USB = models.CharField(max_length=400,null=True,blank=True) #pendiente
	Mailing_country = models.CharField(max_length=400,null=True,blank=True)
	Email = models.EmailField(max_length=400,null=True,blank=True)
	Mobile = models.CharField(max_length=400,null=True,blank=True)
	Cohorte = models.IntegerField(null=True,blank=True)
	Birthdate = models.DateField(null=True,blank=True)
	Age = models.IntegerField(null=True,blank=True)
	Undergrad_degree = models.CharField(max_length=400,null=True,blank=True)
	Graduate_degree = models.CharField(max_length=400,null=True,blank=True)
	Carnet = models.IntegerField(null=True,blank=True)
	USB_undergrad_campus = models.CharField(max_length=30,null=True,blank=True)
	Graduate_campus = models.CharField(max_length=30,null=True,blank=True)
	Work_email = models.EmailField(max_length=400,null=True,blank=True)
	Workplace = models.CharField(max_length=400,null=True,blank=True)
	Donor = models.IntegerField(null=True,blank=True)
	Average_gift = models.FloatField(null=True,blank=True)
	Largest_gift = models.FloatField(null=True,blank=True)
	Smallest_gift = models.FloatField(null=True,blank=True)
	Total_gifts = models.FloatField(null=True,blank=True)
	Best_gift_year_total = models.FloatField(null=True,blank=True)
	Best_gift_year = models.IntegerField(null=True,blank=True)
	Social_networks = models.CharField(max_length=50,null=True,blank=True)
	Twitter_account = models.CharField(max_length=400,null=True,blank=True)
	Instagram_account = models.CharField(max_length=400,null=True,blank=True)
	First_gift_date = models.DateField(null=True,blank=True)
	Last_gift_date = models.DateField(null=True,blank=True)
	Total_number_of_gifts = models.IntegerField(null=True,blank=True)

class User_information(models.Model):
	First_name = models.CharField(max_length=20, default='-')
	Middle_name = models.CharField(max_length=20, default='-')
	Last_name = models.CharField(max_length=20, default='-')
	Mailing_city = models.CharField(max_length=20, default='-')
	Mailing_state = models.CharField(max_length=20, default='-')
	USB_alumn = models.IntegerField(default=0)
	Codigo_Alumn_USB = models.CharField(max_length=20, default='-')
	Mailing_country = CountryField()
	Email = models.EmailField(max_length=40, unique=True)
	Mobile = models.CharField(max_length=20, default='-')
	Cohorte = models.IntegerField(default=0)
	Birthdate = models.DateField()
	Age = models.IntegerField(default=0)
	Undergrad_degree = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in UndergraduateDegreeChoice])
	Graduate_degree = models.CharField(max_length=40)
	Carnet = models.IntegerField(default=0)
	USB_undergrad_campus = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in CampusChoice])
	Graduate_campus = models.CharField(max_length=30, default='-')
	Work_email = models.EmailField(max_length=40)
	Workplace = models.CharField(max_length=20, default='-')
	Donor = models.IntegerField(default=0)
	Social_networks = models.CharField(max_length=50, default='-')
	Twitter_account = models.CharField(max_length=40,default='-')
	Instagram_account = models.CharField(max_length=40, default='-')

	def __str__(self):
		return self.Email

class User_stats(models.Model):
	Email = models.EmailField(max_length=40, unique=True)
	Average_gift = models.FloatField()
	Largest_gift = models.FloatField()
	Smallest_gift = models.FloatField()
	Total_gifts = models.FloatField()
	Best_gift_year_total = models.FloatField()
	Best_gift_year = models.IntegerField()
	First_gift_date = models.DateField()
	Last_gift_date = models.DateField()
	Total_number_of_gifts = models.IntegerField()

	def __str__(self):
		return self.Email

class Achievements(models.Model):
	Name = models.CharField(max_length=30)
	Description = models.CharField(max_length=200)

	def __str__(self):
		return self.Name

class User_Achievements(models.Model):
	Owner = models.ForeignKey(User,on_delete=models.CASCADE)
	Achievement = models.ForeignKey(Achievements,on_delete=models.CASCADE,)
	Date = models.DateField(auto_now_add=True)

	# Falta definir un __str__