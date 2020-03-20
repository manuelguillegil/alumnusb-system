from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login

from accounts.models import User_information, User_stats, Achievements, User_Achievements, Message, Profile_Picture
from accounts.forms import SignUpForm, EditUserDataForm, getUserDataForm
from django.contrib.auth.views import LoginView

from datetime import datetime, timedelta, date

def index(request):
    return render(request,'home.html',{'variable':''})

@login_required
def dashboard(request, username):
    #Check the username and the logged user
    if request.user.username != username:
        return redirect('home')
    
    #try to get the user data if exists
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    #Try to get the user stats:
    usr_stats = get_object_or_404(User_stats, Email=usr.email)

    ach = Achievements.objects.all()

    ach_by_date = []
    ach_by_lvl = []

    for x in ach:
        if User_Achievements.objects.filter(Owner=usr.id,Achievement=x.Name).exists():
            y = User_Achievements.objects.get(Owner=usr.id,Achievement=x.Name)
            ach_by_date.append( (x,y.Date, "../../" + x.Picture.url) )
            ach_by_lvl.append( (x, "../../" + x.Picture.url) )
        
    ach_by_date.sort(key=lambda x:x[1], reverse=True)
    ach_by_lvl.sort(key=lambda x:x[0].Level, reverse=True)

    ach_by_date = ach_by_date[:5]
    ach_by_lvl = ach_by_lvl[:5]

    if Message.objects.filter(Page='Resumen').exists():
        msg = Message.objects.get(Page='Resumen')
    else:
        msg = None

    args = {
                'User_information': user_info,
                'stat': usr_stats,
                'ach_by_date':ach_by_date,
                'ach_by_lvl':ach_by_lvl,
                'msg':msg
            }

    return render(request, 'dashboard/index.html', args)

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

    args = {
                'User_information': user_info,
                'stat': usr_stats
            }

    return render(request, 'dashboard/user_stats.html', args)


def achievements(request, username):

    #Check the username and the loged user
    if request.user.username != username:
        return redirect('home')
    
    #try to get the user data if exists
    usr = get_object_or_404(User, username=username)

    #Try to get the user stats:
    usr_stats = get_object_or_404(User_stats, Email=usr.email)

    usr_info = get_object_or_404(User_information,  Email=usr.email)


    A = Achievements.objects.all()

    ret = []

    for achiev in A:

        if (achiev.Name == 'Numero donaciones bronce'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=5 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Numero donaciones plata'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=10 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Numero donaciones oro'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=20 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Numero donaciones platino'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=30 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Numero donaciones diamante'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=50 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )


        elif (achiev.Name == 'Total donaciones bronce'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_gifts
                if ( n is not None and n>=50 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Total donaciones plata'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_gifts
                if ( n is not None and n>=100 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Total donaciones oro'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_gifts
                if ( n is not None and n>=500 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Total donaciones platino'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_gifts
                if ( n is not None and n>=1000 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Total donaciones diamante'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_gifts
                if ( n is not None and n>=5000 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )


        elif (achiev.Name == 'Donacion estrella bronce'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Largest_gift
                if ( n is not None and n>=100 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Donacion estrella plata'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Largest_gift
                if ( n is not None and n>=200 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Donacion estrella oro'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Largest_gift
                if ( n is not None and n>=300 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Donacion estrella platino'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Largest_gift
                if ( n is not None and n>=500 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

        elif (achiev.Name == 'Donacion estrella diamante'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Largest_gift
                if ( n is not None and n>=1000 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )


        elif (achiev.Name == 'Donante'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                n = usr_stats.Total_number_of_gifts
                if ( n is not None and n>=1 ):
                    new = User_Achievements(Owner=usr,Achievement=achiev)
                    new.save()
                    user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                    ret.append( (achiev, user_ach.Date, True) )
                else:
                    ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )


        elif (achiev.Name == 'Donante recurrente'):
            if not User_Achievements.objects.filter(Owner=usr.id,Achievement=achiev.Name).exists():
                    f = 1
                    n_gifts = usr_stats.Total_number_of_gifts
                    if(n_gifts==None):
                        f = 0
                    start = usr_stats.First_gift_date
                    if(start==None):
                        f = 0
                    last = date.today()
                    if(last==None):
                        f = 0
                    months = ((last - start).days)//30
                    if months == 0 :
                        f = 0
                    if(f==1 and n_gifts/months >= 1):
                        new = User_Achievements(Owner=usr,Achievement=achiev)
                        new.save()
                        user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                        ret.append( (achiev, user_ach.Date, True) )
                    else:
                        ret.append( (achiev, None, False) )
            else:
                user_ach = User_Achievements.objects.get(Owner=usr.id,Achievement=achiev.Name)
                ret.append( (achiev, user_ach.Date, True) )

    ret2 = []

    for i in range(len(ret)):
        ret2.append( (ret[i][0], ret[i][1], ret[i][2], "../../" + ret[i][0].Picture.url) )

    ret2.sort(key=lambda x:x[0].Level, reverse=True)

    args = {
                'achievs':ret2,
                'user_stats':usr_stats, 
                'User_information':usr_info
            }

    return render(request, 'dashboard/user_achievements.html', args)

@login_required
def user_achievs(request, username):

    if request.user.username != username:
        return redirect('home')

    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    return render(request, 'dashboard/user_achievements.html', {'User_information': user_info})

