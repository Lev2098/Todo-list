from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy

from todo_manager.forms import TaskForm
from todo_manager.models import Task, Tag


def index(request:HttpRequest) -> HTTPResponse:
    return  render(request, "todo_manager/index.html",)

class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo_manager/tasks.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        return redirect('todo_manager:task-list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        return redirect('todo_manager:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task

    def form_valid(self, form):
        return redirect('todo_manager:task-list')


class TagViewList(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_manager/tags.html"