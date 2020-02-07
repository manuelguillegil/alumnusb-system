from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import User_information

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditUserDataForm(forms.ModelForm):#UserChangeForm):
    """docstring for EditUserData"""
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = User_information
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Mailing_city',
            'Mailing_state',
            'USB_alumn',
            #'Codigo_Alumn_USB',
            'Mailing_country',
            #'Email',
            'Mobile',
            'Cohorte',
            'Birthdate',
            'Age',
            'Undergrad_degree',
            'Graduate_degree',
            'Carnet',
            'USB_undergrad_campus',
            'Graduate_campus',
            'Work_email',
            'Workplace',
            'Donor',
            'Social_networks',
            'Twitter_account',
            'Instagram_account'
        )


class getUserDataForm(forms.ModelForm):#UserChangeForm):
    """docstring for EditUserData"""
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = User_information
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Mailing_city',
            'Mailing_state',
            'USB_alumn',
            #'Codigo_Alumn_USB',
            'Mailing_country',
            #'Email',
            'Mobile',
            'Cohorte',
            'Birthdate',
            'Age',
            'Undergrad_degree',
            'Graduate_degree',
            'Carnet',
            'USB_undergrad_campus',
            'Graduate_campus',
            'Work_email',
            'Workplace',
            'Donor',
            'Social_networks',
            'Twitter_account',
            'Instagram_account'
        )