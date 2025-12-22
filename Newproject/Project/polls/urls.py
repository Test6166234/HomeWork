from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks_list, name="tasks_list"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("completed/", views.completed_tasks, name="completed_tasks"),
]
