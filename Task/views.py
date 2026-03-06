
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

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
    return render(request , 'auth/signup.html')

def Login(request):
    if request.method =='POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(request, username=Username, password = Password) # if existe return user else return None
        if user is not None:
            login(request , user) # login() : creates a session for the user and sets the appropriate cookies in the user's browser to maintain the logged-in state across requests.
            return redirect('app/inbox.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request , 'auth/login.html')


def Logout(request):
    logout(request)  # ← deletes the session from DB + clears the cookie
    return redirect('index')

@login_required(login_url='login') 
def AddTask(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) # commit=False : create an instance of the model but do not save it to the database yet
            task.user = request.user   # add the user manually to the task instance before saving it to the database.
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('app/inbox.html')
    return render(request , 'app/task_form.html' , {'form': TaskForm()})

@login_required(login_url='login') 
def task_detail(request , task_id):
    task = Task.objects.get(id=task_id , user= request.user) 
    return render(request , 'app/task_detail.html' , {'task': task})

@login_required(login_url='login') 
def task_delete(request , task_id):
    task = Task.objects.get(id=task_id , user= request.user)  # If the user is not authenticated, it assigns None to task.
    if request.method == 'POST':
     task.delete()
     messages.success(request, 'Task deleted successfully.')
     return redirect('app/inbox.html')
    return render(request , 'app/task_confirm_delete.html' , {'task': task})

@login_required(login_url='login') 
def task_update(request , task_id):
    task = Task.objects.get(id=task_id , user= request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task) # instance=task : This allows the user to see the current values and make changes as needed.
        if form.is_valid():
            task = form.save(commit=False) # build a new obj 
            task.user = request.user
            task.save() 
            messages.success(request, 'Task updated successfully.')
            return redirect('app/inbox.html')
    return render(request , 'app/task_form.html' , {'task': task , 'form': TaskForm(instance=task)})
@login_required(login_url='login')
def task_toggle(request , task_id):
    task = Task.objects.get(id=task_id , user= request.user)
    task.is_done = not task.is_done
    task.save()
    return redirect('app/inbox.html')

def Tasks(request):
    res = Task.objects.filter(user=request.user) if request.user.is_authenticated else [] # If the user is not authenticated, it assigns an empty list to res.
    return render(request , 'index.html' , {'tasks': res})