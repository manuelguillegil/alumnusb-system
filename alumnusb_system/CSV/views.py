import csv, io, datetime
from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404


@login_required
def profile_upload(request):
	if ( request.user.is_authenticated and request.user.is_staff):    
		template = "profile_upload.html"
		prompt = {
			'title': 'El orden del CSV deberia ser',
			'info': 'Account ID -> First Name -> Middle Name -> Last Name -> Mailing City -> Mailing State/Province -> USB Alumn -> Codigo AlumnUSB -> Mailing Country -> Email -> Mobile -> Cohorte -> Birthdate -> Age -> Undergrad Degree -> Graduate Degree -> Carnet -> USB Undergrad Campus -> Graduate Campus -> Work Email -> Workplace -> Donor -> Average Gift -> Largest Gift -> Smallest Gift -> Total Gifts -> Best Gift Year Total -> Best Gift Year -> Social Networks -> Twitter Account -> Instagram Account -> First Gift Date -> Last Gift Date -> Total Number of Gifts'
				  }
	
		if request.method == "GET":
			return render(request, template, prompt)    
	
		csv_file = request.FILES['file']    
		
		if not csv_file.name.endswith('.csv'):
			return render(request, template, prompt)    

		data_set = csv_file.read().decode('UTF-8') 
		io_string = io.StringIO(data_set)
		next(io_string)
		for column in csv.reader(io_string, delimiter=',', quotechar="|"):
			if ( len(column) < 34 ):
				error = len(column)
				return render(request, template, {'title':error})
			
			User_information.objects.filter(Email=column[9]).delete()
			User_stats.objects.filter(Email=column[9]).delete()
			
			created2 = User_information.objects.update_or_create(
			First_name=column[1],
			Middle_name=column[2],
			Last_name=column[3],
			Mailing_city=column[4],
			Mailing_state=column[5],
			USB_alumn=is_bool(column[6]),
			Codigo_Alumn_USB=column[7],
			Email=column[9],
			Mobile=column[10],
			Cohorte=is_int(column[11]),
			Birthdate=transform_date(column[12]),
			Age=is_int(column[13]),
			Graduate_degree=column[15],
			Carnet=is_int(column[16]),
			Graduate_campus=column[18],
			Work_email=column[19],
			Workplace=column[20],
			Donor=is_bool(column[21]),
			Social_networks=column[28],
			Twitter_account=column[29],
			Instagram_account=column[30]
			)

			created = User_stats.objects.update_or_create(
			Email=column[9],
			Average_gift=is_float(column[22]),
			Largest_gift=is_float(column[23]),
			Smallest_gift=is_float(column[24]),
			Total_gifts=is_float(column[25]),
			Best_gift_year_total=is_float(column[26]),
			Best_gift_year=is_int(column[27]),
			First_gift_date=transform_date(column[31]),
			Last_gift_date=transform_date(column[32]),
			Total_number_of_gifts=is_int(column[33])
			)
		return render(request, template, {'title':"La carga fue exitosa"})
	else:
		return redirect('home')



## Functions to help the csv loader
def is_int(x):
	if (x==''):
		return 0
	return x

def is_float(x):
	if (x==''):
		return 0.0
	return x

def transform_date(x):
	if (x==''):
		return '2020-01-01'
	return datetime.datetime.strptime(x, '%m/%d/%Y').strftime('%Y-%m-%d')

def is_bool(x):
	if (x=='1'):
		return True
	else:
		return False
	