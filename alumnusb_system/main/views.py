from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'home.html',{'variable':''})

def user_data(request):
    return render(request, 'user_data.html', {'var':''})
