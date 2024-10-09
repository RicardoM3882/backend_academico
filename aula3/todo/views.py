from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo 
    fields = ["title", "deadline"] 
    success_url = reverse_lazy("todo_list")