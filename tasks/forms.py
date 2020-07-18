from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a task' , 'size': '5'}))

    class Meta:
        model = Task
        fields = "__all__"