from django.shortcuts import redirect , render
from django.http import HttpResponse
from .forms import RegistrationForm , UserUpdateForm , ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() #automatically hashes the password
            messages.success(request , f'Successfully created an account for {form.cleaned_data["username"]} , please login <a href = "http://127.0.0.1:8000/profile/login/">here</a>')
            return redirect('homepage')
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request , 'users/register.html' , context)


@login_required(login_url = '/profile/login') #if the users is not logged in , it redirects them to the login page
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance=current_user)
        p_form = ProfileUpdateForm(request.POST , request.FILES,instance=current_user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , 'Your profile has been updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=current_user)
        p_form = ProfileUpdateForm()

    image_url = Profile.objects.filter(user_id = current_user.id)[0].filename()
    context = {'url':  image_url , 'u_form' : u_form , 'p_form' : p_form}
    return render(request , 'users/profile.html' , context)

#Can use default django provided view

def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        auth_login(request , user)
        messages.success(request , f'Successfully logged in as {form.cleaned_data["username"]}')
        return redirect('homepage')
    context = {'form' : form}
    return render(request , 'users/login.html' , context)


def logout(request): 
    auth_logout(request)
    return render(request , 'users/logout.html')