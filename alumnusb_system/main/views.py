from django.shortcuts import render
from django.http import HttpResponse


def index(request):
<<<<<<< Updated upstream
    return render(request,'home.html',{'variable':''})

def user_data(request):
    return render(request, 'user_data.html', {'var':''})
=======
    return render(request,'home.html',{'variable':'Start Bootstrap'})
>>>>>>> Stashed changes
