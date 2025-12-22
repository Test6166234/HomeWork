# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('settings/reset/', views.reset_tasks, name='reset_tasks'),
    path('api/update_step/<int:step_id>/', views.update_task_step, name='update_task_step'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/toggle_done/', views.toggle_task_done, name='toggle_task_done'),

    # Маршрут для создания с указанием статуса
    path('create_with_status/<str:status>/', views.create_task, name='create_task_with_status'),
]

