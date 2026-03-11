from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing , name='landing'),
    path('tasks/add-task/', views.AddTask , name='AddTask'),
    path('logout/', views.Logout, name='logout'),
    path('tasks/<int:task_id>/', views.task_detail, name='TaskDetail'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='TaskDelete'),
    path('tasks/<int:task_id>/update/', views.task_update, name='TaskUpdate'),
    path('tasks/<int:task_id>/toggle/', views.task_toggle, name='TaskToggle'),
    path('inbox/' , views.Tasks , name='inbox'),
    path('taday/', views.Today ,name="today"),
    path('completed/',views.Completed,name="completed")

]