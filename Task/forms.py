from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desciption',  'priority', 'due_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Task title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form__input',
                'placeholder': 'Description (optional)',
                'rows': 3
            }),
            
            'priority': forms.Select(attrs={
                'class': 'form__select'
            }),
            'category': forms.Select(attrs={
                'class': 'form__select'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form__input',
                'type': 'date'        # renders as date picker in browser
            }),
            'is_done': forms.CheckboxInput(attrs={
                'class': 'form__checkbox'         }),
        }
        