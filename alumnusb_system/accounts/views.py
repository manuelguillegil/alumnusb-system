from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from .models import User_information
from .forms import SignUpForm, EditUserDataForm, getUserDataForm

# Quitar esta view luego
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            if not User_information.filter(Email=user.email).exists():
                user1inf = User_information(First_name='Luis',Middle_name='Algo',
                    Last_name='Dias',Mailing_city='Caracas',USB_alumn=1,
                    Codigo_Alumn_USB='1234',Mailing_country='Venezuela',
                    Email=user.email,Mobile='03013201',Cohorte=15,Birthdate=1/1/1990,
                    Age=20,Undergrad_degree='compu',Graduate_degree='compu',Carnet='1511540',
                    USB_undergrad_campus='Sartenejar',Graduate_campus='sartenejas',Work_email='',
                    Workplace='',Donor=1,Social_networks='tw,ig,fc',Twitter_account='ldiaz',
                    Instagram_account='ldiaz')
                user1inf.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not User_information.objects.filter(Email=user.email).exists():
                user1inf = User_information(First_name='',Middle_name='',
                    Last_name='D',Mailing_city='',USB_alumn=0,
                    Codigo_Alumn_USB='',Mailing_country='',
                    Email=user.email,Mobile='',Cohorte=0,Birthdate='2020-1-1',
                    Age=1,Undergrad_degree='',Graduate_degree='',Carnet=0,
                    USB_undergrad_campus='',Graduate_campus='',Work_email='',
                    Workplace='',Donor=1,Social_networks='',Twitter_account='',
                    Instagram_account='')
                user1inf.save()
            return redirect('login_url')
    else:
        form = SignUpForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def edit_user_data(request, username):

    if request.user.username != username:
        return redirect('home')
    
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    if request.method == 'POST':
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('edit_user_data_test', request.user.username)  
    else:
        form = EditUserDataForm(instance=user_info)

    return render(request, 'edit_user_data.html', {'User_information': user_info, 'form': form})
#Esta es una función de prueba para la pág de edit_user_data
@login_required
def edit_user_data_test(request, username):

    if request.user.username != username:
        return redirect('home')
    """ xd """
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    if request.method == 'POST':
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('Datos Personales')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'user_data.html', {'User_information': user_info, 'form': form})



@login_required
def get_user_data(request, username):

    if request.user.username != username:
        return redirect('home')
    
    if request.method == 'POST':
        form = getUserDataForm(request.POST)
        if form.is_valid():
            usr_info = form.save()
            usr_info.Email = request.user.email
            usr_info.save()
            return redirect('Datos Personales')  
    else:
        form = getUserDataForm()

    return render(request, 'get_user_data.html', {'form': form})
    