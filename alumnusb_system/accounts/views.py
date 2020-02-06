from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


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

def registerView(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form = SignUpForm()
	return render(request,'registration/register.html',{'form':form})