from django import forms
from .models import Todo

class Todoapp(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name','task',)

        labels = {
            'name':"User",
            'task':"Task",
        }