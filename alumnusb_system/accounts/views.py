from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login

from .models import User_information, User_stats, Profile_Picture
from .forms import SignUpForm, EditUserDataForm, getUserDataForm, pictureId
from django.contrib.auth.views import LoginView

@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not User_information.objects.filter(Email=user.email).exists():
                user1inf = User_information(First_name='',Middle_name='',
                    Last_name='',Mailing_city='',USB_alumn=0,
                    Codigo_Alumn_USB='',Mailing_country='',
                    Email=user.email,Mobile='',Cohorte=0,Birthdate='2020-1-1',
                    Age=1,Undergrad_degree='',Graduate_degree='',Carnet=0,
                    USB_undergrad_campus='',Graduate_campus='',Work_email='',
                    Workplace='',Donor=1,Social_networks='',Twitter_account='',
                    Instagram_account='')
                user1inf.save()
            if not User_stats.objects.filter(Email=user.email).exists():
                user1stats = User_stats(Email=user.email,Average_gift=0,
                    Largest_gift=0,Smallest_gift=0,Total_gifts=0,
                    Best_gift_year_total=0,Best_gift_year=0, First_gift_date='2020-1-1', Last_gift_date='2020-1-1', Total_number_of_gifts=0)
                user1stats.save()
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
            return redirect('user_data', request.user.username)  
    else:
        form = EditUserDataForm(instance=user_info)

    return render(request, 'edit_user_data.html', {'User_information': user_info, 'form': form})

@login_required
def user_data(request, username):

    if request.user.username != username:
        return redirect('home')

    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    ret_all_pics = []
    all_pictures = Profile_Picture.objects.all()
    for p in all_pictures:
        ret_all_pics.append(( p , "/"+ p.Picture.url ))


    if ( user_info.Picture != None ):
        pic = Profile_Picture.objects.get(id=user_info.Picture.id)
        ret_pic = ( "/"+ pic.Picture.url , True, pic.id )
    else:
        ret_pic = ( "" , False , -1)

    form = pictureId()

    args = {
            'User_information': user_info, 
            'pic': ret_pic,
            'prof_pics':ret_all_pics,
            'form': form
            }

    return render(request, 'user_data.html', args)

@login_required
def edit_user_picture(request, username):

    if request.user.username != username:
        return redirect('home')
    
    usr = get_object_or_404(User, username=username)
    user_info = get_object_or_404(User_information,  Email=usr.email)

    if request.method == 'POST':
        form = pictureId(request.POST)
        pic_id = form.data['Pic_id']
        if Profile_Picture.objects.filter(id=pic_id).exists():
            pic = Profile_Picture.objects.get(id=pic_id)
            user_info.Picture = pic
            user_info.save()
            return redirect('user_data', request.user.username)  
        else:
            form = pictureId()
    else:
        form = pictureId()

    return render(request, 'edit_user_picture.html', {'form': form})