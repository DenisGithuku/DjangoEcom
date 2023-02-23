from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def home(request):
    return HttpResponse("This is the homepage")


def login(request):
    if request.method =='POST':
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            
            # check if the user is already in database
            username = login_form.cleaned_data['username']
            user = models.UserModel.objects.get(username=username)

            # check if the user object is null or not
            if (user.DoesNotExist is True):
                return redirect('register')
            else:
                return redirect('home')
    else:
        login_form = forms.UserLoginForm()
    context = {
        'login_form': login_form
    }

    return render(request=request, template_name='login.html', context=context)

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()            
            return redirect('login')
    else:
        register_form = forms.RegisterForm()

    context = {
        'register_form': register_form
    }
    return render(request=request, template_name = 'register.html', context = context)

def check_email(request):
    if request.method == "POST":
        email_form = forms.CheckEmail(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            user = models.UserModel.objects.get(email=email)
            if (user.DoesNotExist is True):
                return redirect("register")
            else:
                return redirect("reset_password", email)
    else:
        email_form = forms.CheckEmail()
    context = {
        'email_form': email_form
    }
    return render(request=request, template_name='confirm_email.html', context = context)

def reset_password(request, email):
    if request.method == "POST":
        reset_password_form = forms.ResetPassword(request.POST)
        if reset_password_form.is_valid():
            # strip password from the form
            password = reset_password_form.cleaned_data['password']

            # get the user with the supplied email
            user = models.UserModel.objects.get(email=email)
            
            # set the user password to the new password
            user.password = password

            # save user
            user.save()
            return redirect('login')
    else:
        reset_password_form = forms.ResetPassword()
    context = {
        'reset_password_form': reset_password_form
    }
    return render(request = request, template_name = "reset_password.html", context = context)
        
