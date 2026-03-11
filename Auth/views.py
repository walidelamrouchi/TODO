from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def Signup(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('ConfirmPassword')
        Username = request.POST.get('Username')
        if User.objects.filter(username=Username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup') # PRG: post->redirect->get pattern to prevent form resubmission on page refresh
        if Password != ConfirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        user = User.objects.create_user(Username, Email, Password) # create_user() : creates a new user with the given username, email, and password. It also handles password hashing and other necessary setup for the user account.
        user.first_name = FirstName
        user.last_name = LastName
        user.save()
        return redirect('login')
    return render(request , 'auth/login.html')

def Login(request):
    if request.method =='POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(request, username=Username, password = Password) # if existe return user else return None
        if user is not None:
            login(request , user) # login() : creates a session for the user and sets the appropriate cookies in the user's browser to maintain the logged-in state across requests.
            return redirect('inbox')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request , 'auth/login.html')
