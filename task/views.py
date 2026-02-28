from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm

# Представлення списику існуючих завдань
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/task_list.html"


# Представлення деталей конкретного завдання
class TaskDetailView(DetailView):
    model = Task 
    context_object_name = "task"
    template_name = "task/task_detail.html"


# Створення нової задачі
class TaskCreateView(CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    # перевизначаємо метод form_valid
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

# Редагування нової задачі
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")