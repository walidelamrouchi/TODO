from django.db import models
from django.contrib.auth.models import User #class user permet de gere , cree et auth user
# Create your models here.

#class Category
class Category(models.Model):
    CATEGORY = [(1 ,'personal') , (2,'agency') , (3,'student')]
    name = models.IntegerField(choices=CATEGORY)
    def __str__(self):
        return self.get_name_display() # get_name_display() : cherche ettiquate correspondant de liste
    
    
# class task
class Task(models.Model):
    PRIORITY = [(1 , 'low') , (2 , 'medium') , (3 , 'high')]
    title  = models.CharField()
    desciption  = models.CharField()
    is_done = models.BooleanField()
    priority = models.IntegerField(choices=PRIORITY)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True , blank=True)
    user_id = models.ForeignKey(User , on_delete= models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    
    
    