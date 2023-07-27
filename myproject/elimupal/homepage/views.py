from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('registration')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    
    return render(request, 'accounts/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Renamed the login function
            return redirect('dashboard1')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'accounts/login.html')




def registration(request):
    return render(request, 'accounts/registration.html') 



    