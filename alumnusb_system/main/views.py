from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login

from accounts.models import User_information, User_stats
from accounts.forms import SignUpForm, EditUserDataForm, getUserDataForm
from django.contrib.auth.views import LoginView

def index(request):
    return render(request,'home.html',{'variable':''})

@login_required
def dashboard(request, username):
    #Check the username and the loged user
    if request.user.username != username:
        return redirect('home')
    
    #try to get the user data if exists
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    #Try to get the user stats:
    usr_stats = get_object_or_404(User_stats, Email=usr.email)

    if request.method == 'POST':
        
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('user_data')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'dashboard/index.html', {'User_information': user_info, 'form': form, 'stat':usr_stats})

@login_required
def user_stats(request, username):
    #Check the username and the loged user
    if request.user.username != username:
        return redirect('home')
    
    #try to get the user data if exists
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    #Try to get the user stats:
    usr_stats = get_object_or_404(User_stats, Email=usr.email)

    if request.method == 'POST':
        
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('user_data')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'dashboard/user_stats.html', {'User_information': user_info, 'form': form, 'stat':usr_stats})