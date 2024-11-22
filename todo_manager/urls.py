from .views import (index,
                    TaskListView,
                    TaskUpdateView,
                    TaskDeleteView,
                    TaskCreateView,
                    TaskUndoView,
                    TaskCompleteView,
                    TagListView,
                    TagCreateView,
                    TagUpdateView,
                    TagDeleteView,
                    )
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
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
    path(
        "tasks/<int:pk>/complete/",
        TaskCompleteView.as_view(),
        name="task-complete"
    ),
    path(
        "tasks/<int:pk>/undo/",
        TaskUndoView.as_view(),
        name="task-undo"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todo_manager"
