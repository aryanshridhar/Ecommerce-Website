#Creating my own usercreationform 

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Refer django docs

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20 ,required = True , widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    last_name = forms.CharField(max_length = 30 , required=True , widget= forms.TextInput(attrs={
        'class':  'form-control'
    }))
    email = forms.EmailField(required=True , widget=forms.EmailInput(attrs={
        'class':  'form-control'
    }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )
    
    def save(self , commit = True):   #Commit  =  True will save the data in database
        user = super(RegistrationForm , self).save(commit=False) 
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']