from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from .models import User_information
from .forms import SignUpForm, EditUserDataForm

# Quitar esta view luego
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
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
            form.save()
            return redirect('login_url')
    else:
        form = SignUpForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def edit_user_data(request, username):

    if request.user.username != username:
        return redirect('home')
    """ xd """
    usr = get_object_or_404(User, username=username);
    user_info = get_object_or_404(User_information,  Email=usr.email);

    if request.method == 'POST':
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('Datos Personales')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'edit_user_data.html', {'User_information': user_info, 'form': form})
#Esta es una función de prueba para la pág de edit_user_data
@login_required
def edit_user_data_test(request, username):

    if request.user.username != username:
        return redirect('home')
    """ xd """
    usr = get_object_or_404(User, username=username);
    user_info = get_object_or_404(User_information,  Email=usr.email);

    if request.method == 'POST':
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('Datos Personales')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'user_data.html', {'User_information': user_info, 'form': form})


"""
@login_required
def get_user_data(request, username):

    if request.user.username != username:
        return redirect('home')
    
    #usr = get_object_or_404(User, username=username);
    #user_info = get_object_or_404(User_information,  Email=usr.email);

    if request.method == 'POST':
        form = getUserDataForm(request.POST)#, #instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('Datos Personales')  
    else:
        form = getUserDataForm()#instance=user_info)
    return render(request, 'edit_user_data.html', {'User_information': user_info, 'form': form})
    """