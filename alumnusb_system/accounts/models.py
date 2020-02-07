from django.db import models
from django.contrib.auth.models import User

# Model to upload the AlumnUSB fields to our database
class alumncsv(models.Model):
	First_name = models.CharField(max_length=20)
	Middle_name = models.CharField(max_length=20)
	Last_name = models.CharField(max_length=20)
	Mailing_city = models.CharField(max_length=20)
	Mailing_state = models.CharField(max_length=20)
	USB_alumn = models.IntegerField()
	Codigo_Alumn_USB = models.CharField(max_length=20) #pendiente
	Mailing_country = models.CharField(max_length=20)
	Email = models.EmailField(max_length=40, unique=True)
	Mobile = models.CharField(max_length=20)
	Cohorte = models.IntegerField()
	Birthdate = models.DateField()
	Age = models.IntegerField()
	Undergrad_degree = models.CharField(max_length=40)
	Graduate_degree = models.CharField(max_length=40)
	Carnet = models.IntegerField()
	USB_undergrad_campus = models.CharField(max_length=30)
	Graduate_campus = models.CharField(max_length=30)
	Work_email = models.EmailField(max_length=40)
	Workplace = models.CharField(max_length=20)
	Donor = models.IntegerField()
	Average_gift = models.FloatField()
	Largest_gift = models.FloatField()
	Smallest_gift = models.FloatField()
	Total_gifts = models.FloatField()
	Best_gift_year_total = models.FloatField()
	Best_gift_year = models.IntegerField()
	Social_networks = models.CharField(max_length=50)
	Twitter_account = models.CharField(max_length=40)
	Instagram_account = models.CharField(max_length=40)
	First_gift_date = models.DateField()
	Last_gift_date = models.DateField()
	Total_number_of_gifts = models.IntegerField()

class User_information(models.Model):
	First_name = models.CharField(max_length=20)
	Middle_name = models.CharField(max_length=20)
	Last_name = models.CharField(max_length=20)
	Mailing_city = models.CharField(max_length=20)
	Mailing_state = models.CharField(max_length=20)
	USB_alumn = models.IntegerField()
	Codigo_Alumn_USB = models.CharField(max_length=20)
	Mailing_country = models.CharField(max_length=20)
	Email = models.EmailField(max_length=40, unique=True)
	Mobile = models.CharField(max_length=20)
	Cohorte = models.IntegerField()
	Birthdate = models.DateField()
	Age = models.IntegerField()
	Undergrad_degree = models.CharField(max_length=40)
	Graduate_degree = models.CharField(max_length=40)
	Carnet = models.IntegerField()
	USB_undergrad_campus = models.CharField(max_length=30)
	Graduate_campus = models.CharField(max_length=30)
	Work_email = models.EmailField(max_length=40)
	Workplace = models.CharField(max_length=20)
	Donor = models.IntegerField()
	Social_networks = models.CharField(max_length=50)
	Twitter_account = models.CharField(max_length=40)
	Instagram_account = models.CharField(max_length=40)

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