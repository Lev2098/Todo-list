from .views import index, TaskViewList, TagViewList, TaskUpdateView, TaskDeleteView, TaskCreateView
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskViewList.as_view(), name="task-list"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"),
    path("tags/", TagViewList.as_view(), name="tag-list"),
]

app_name = "todo_manager"