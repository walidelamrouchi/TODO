from django.db import models
from django.contrib.auth.models import User #class user permet de gere , cree et auth user
# Create your models here.

#class Category
class Category(models.Model):
    CATEGORY = [(1 ,'Personal'),
                (2,'Work'),
                (3,'Home Improvement'),
                ]
    name = models.IntegerField(choices=CATEGORY)
    def __str__(self):
        return self.get_name_display() # get_name_display() : cherche ettiquate correspondant de liste
    

    
# class task
class Task(models.Model):
    PRIORITY = [
                (1 , 'Priority 1'),
                (2 , 'Priority 2'),
                (3 , 'Priority 3'),                                                   
                (4 , 'Priority 4'),                                                   
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY , default=1)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True , blank=True)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True)
    def __str__(self):
        return self.title
    
    
    