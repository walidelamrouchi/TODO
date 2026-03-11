from django import forms
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',  'priority', 'due_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'task-card__title-input',
                'placeholder': 'Task name',
                'autofocus': True
            }),
            'description': forms.TextInput(attrs={
                'class': 'task-card__desc-input',
                'placeholder': 'Description',
            }),
            'priority': forms.Select(attrs={
                'class': 'task-card__select',
                'id': 'prioritySelect'
            }),
            'category': forms.Select(attrs={
                'class': 'task-card__select',
                'id': 'categorySelect'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'task-card__date',
                'type': 'date',
                'id': 'dueDateInput',
                'onclick': 'this.showPicker()',
                'min': timezone.now().date(),
            }),    
        }
        