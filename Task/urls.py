from django.urls import path
from . import views
urlpatterns = [
    path('inbox' , views.Tasks , name='inbox'),
    path('login', views.Login , name='login'),
    path('signup', views.Signup , name='signup'),
    path('tasks/add-task/', views.AddTask , name='AddTask'),
    path('logout/', views.Logout, name='logout'),
    path('tasks/<int:task_id>/', views.task_detail, name='TaskDetail'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='TaskDelete'),
    path('tasks/<int:task_id>/update/', views.task_update, name='TaskUpdate'),
    path('tasks/<int:task_id>/toggle/', views.task_toggle, name='TaskToggle'),
    

]