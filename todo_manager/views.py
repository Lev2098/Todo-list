from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View

from .forms import TaskForm
from .models import Task, Tag


def index(request:HttpRequest) -> HTTPResponse:
    return  render(request, "todo_manager/index.html",)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo_manager/tasks.html"
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task


class TaskCompleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = True
        task.save()
        return redirect('todo_manager:task-list')


class TaskUndoView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect('todo_manager:task-list')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_manager/tags.html"
    paginate_by = 3


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "/tags/"
