
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.



def Logout(request):
    logout(request)  # ← deletes the session from DB + clears the cookie
    return redirect('landing')

@login_required(login_url='login') 
def AddTask(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) # commit=False : create an instance of the model but do not save it to the database yet
            task.user = request.user   # add the user manually to the task instance before saving it to the database.
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('inbox')
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
     return redirect('inbox')
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
            return redirect('inbox')
    return render(request , 'app/task_update.html' , {'task': task , 'form': TaskForm(instance=task)})
@login_required(login_url='login')
def task_toggle(request , task_id):
    task = Task.objects.get(id=task_id , user= request.user)
    task.is_done = not task.is_done
    task.save()
    return redirect(request.META.get('HTTP_REFERER' , 'inbox')) #browser request contains headers — metadata about the request. One of them is `HTTP_REFERER` — the URL of the page that sent the request.

def Tasks(request):
    res = Task.objects.filter(user=request.user) if request.user.is_authenticated else [] # If the user is not authenticated, it assigns an empty list to res.
    return render(request , 'app/inbox.html' , {'tasks': res})

def Today(request):
    TaskToday = Task.objects.filter(user = request.user , is_done = False , due_date__date = timezone.now().date()) #only today task
    return render(request, 'app/today.html', {'TaskToday' : TaskToday})
def Completed(request):
    TaskCompleted = Task.objects.filter(user = request.user , is_done=True)
    return render(request , 'app/completed.html' ,{'TaskCompleted':TaskCompleted})

def landing(request):
    # if already logged in → skip landing → go to inbox
    if request.user.is_authenticated:
        return redirect('inbox')
    return render(request, 'landing.html')