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

from datetime import datetime, timedelta

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
    #usr_stats = get_object_or_404(User_stats, Email=usr.email)
    

    if request.method == 'POST':
        
        form = EditUserDataForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('user_data')  
    else:
        form = EditUserDataForm(instance=user_info)
    return render(request, 'dashboard/index.html', {'User_information': user_info, 'form': form})


def achievements(request, username):

    #Check the username and the loged user
    if request.user.username != username:
        return redirect('home')
    
    #try to get the user data if exists
    usr = get_object_or_404(User, username=username)

    #Try to get the user stats:
    usr_stats = get_object_or_404(User_stats, Email=usr.email)

    lnd = " Logro no desbloqueado "

    # q is for stats from the db, i for moving through the lists and
    # f to mark null values

    # reach x $
    f = 1
    i = 0
    ans1 = "Logro no desbloqueado"
    q = usr_stats.Total_gifts
    if(q==None):
        f = 0

    for x in [50, 100, 500, 1000, 5000]:
        if(f==1  and x <= q):
            ans1 = "LLegaste a %d dolares!",x
        i += 1


    # number of gifts, reach y
    f = 1
    i = 0
    ans2 =  "Logro no desbloqueado"
    q = usr_stats.Total_number_of_gifts
    if(q==None):
        f = 0

    for y in [5, 10, 20, 30, 50]:
        if(f==1 and q >= y):
            ans2 = " LLegaste a %d donaciones! ", y
        i+=1

    # Star gitf, make a gift larger than x
    f = 1
    i = 0
    ans3 =  "Logro no desbloqueado"
    q = usr_stats.Largest_gift
    if(q==None):
        f = 0

    for x in [100, 200, 300, 500, 1000]:
        if(f==1 and q >= x):
            ans3 = " Donacion estrella! %d", x
        i += 1


    # First gift
    q = usr_stats.First_gift_date
    if(q != None):
        ans4 = " Has donado por primera vez! "
    else:
        ans4 =  "Logro no desbloqueado"

    # frequent donor
    f = 1
    n_gifts = usr_stats.Total_number_of_gifts
    if(n_gifts==None):
        f = 0
    start = usr_stats.First_gift_date
    if(start==None):
        f = 0
    last = usr_stats.Last_gift_date
    if(last==None):
        f = 0
    months = ((last - start).days)//30
    if months == 0 :
        f = 0
    if(f==1 and n_gifts/months >= 1):
        ans5 = " Donante frecuente! "
    else:
        ans5=  "Logro no desbloqueado"

    args = {'ach1': ans1, 'ach2': ans2, 'ach3': ans3, 'ach4': ans4, 'ach5': ans5}

    return render(request, 'achievements.html', args)