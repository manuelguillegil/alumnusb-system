import csv, io
from django.shortcuts import render
from accounts.models import *
from django.contrib import messages

# Create your views here.# one parameter named request
def profile_upload(request):    # declaring template
	template = "profile_upload.html"
	data = alumncsv.objects.all()# prompt is a context variable that can have different values      depending on their context
	prompt = {
		'order': 'Order of the CSV should be name, email, address,    phone, profile',
		'profiles': data    
			  }
	# GET request returns the value of the data with the specified key.
	if request.method == "GET":
		return render(request, template, prompt)    

	csv_file = request.FILES['file']    # let's check if it is a csv file
	
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')    

	data_set = csv_file.read().decode('UTF-8') 
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = alumncsv.objects.update_or_create(
			Account_id=column[0],
			First_name=column[1],
			Middle_name=column[2],
			Last_name=column[3],
			Mailing_city=column[4],
			Mailing_state=column[5],
			USB_alumn=isInt(column[6]),
			Codigo_Alumn_USB=column[7],
			Mailing_country=column[8],
			Email=column[9],
			Mobile=column[10],
			Cohorte=isInt(column[11]),
			Birthdate='2020-01-01',
			Age=isInt(column[13]),
			Undergrad_degree=column[14],
			Graduate_degree=column[15],
			Carnet=isInt(column[16]),
			USB_undergrad_campus=column[17],
			Graduate_campus=column[18],
			Work_email=column[19],
			Workplace=column[20],
			Donor=isInt(column[21]),
			Average_gift=isFloat(column[22]),
			Largest_gift=isFloat(column[23]),
			Smallest_gift=isFloat(column[24]),
			Total_gifts=isFloat(column[25]),
			Best_gift_year_total=isFloat(column[26]),
			Best_gift_year=isInt(column[27]),
			Social_networks=column[28],
			Twitter_account=column[29],
			Instagram_account=column[30],
			First_gift_date=column[31],
			Last_gift_date=column[32],
			Total_number_of_gifts=isInt(column[33])
		)
	context = {}
	return render(request, template, context)


def isInt(x):
	if (type(x)==type(5)):
		return x
	return 0

def isFloat(x):
	if (type(x)==type(5.5)):
		return x
	return 0.0