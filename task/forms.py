from django import forms
from .models import Task

# Форма для створення\редагування задач
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "deadline"]