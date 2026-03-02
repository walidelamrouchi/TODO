
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.

def Task(request):
    
    return render(request , 'todo/index.html')

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
            return redirect('signup') #PRG pattern to avoid resubmission of form data on page refresh
        if Password != ConfirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        user = User.objects.create_user(Username, Email, Password)
        user.first_name = FirstName
        user.last_name = LastName
        user.save()
        return redirect('login')
    return render(request , 'todo/auth/signup.html')

def Login(request):
    if request.method =='POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(request, username=Username, password = Password) # if existe return user else return None
        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
            
    return render(request , 'todo/auth/login.html')