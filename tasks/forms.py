from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'completed']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter task name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter task description'}),
            'due_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
        }