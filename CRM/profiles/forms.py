from django import forms
from .models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','descriptions','task_date','task_time']
        widgets = {
            'task_date': forms.DateInput(attrs={'type': 'date'}),
            'task_time': forms.TimeInput(attrs={'type': 'time'}),
        }