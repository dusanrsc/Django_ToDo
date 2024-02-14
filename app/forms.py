from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "done"] # or "__all__" 'thunder all' for all fields

        labels = {
            "title": "",
            "done": "",
        }

        widgets = {
            "title": forms.TextInput(attrs={"placeholder":"Task Title", "class":"form-control", "style": "width:350px"}),
            "done": forms.CheckboxInput(attrs={"class": "form-check"}),
            
        }