# polls/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Exists, OuterRef
from .models import Task, TaskStep
# from .forms import TaskForm  <-- Эта строка удалена

import json


# Функция-хелпер для импорта формы внутри функций
def get_task_form():
    from .forms import TaskForm
    return TaskForm


# -------------------- Задачи --------------------

def tasks_list(request):
    """
    Основное представление доски задач (Kanban-доска).
    """
    all_active_tasks = Task.objects.filter(is_done=False)

    # order_by('order') удалено из всех фильтров
    tasks_in_progress = all_active_tasks.filter(taskstep__done=True).distinct()
    tasks_planned = all_active_tasks.exclude(
        Exists(TaskStep.objects.filter(task=OuterRef('pk'), done=True))
    )
    tasks_done = Task.objects.filter(is_done=True)

    task_columns = [
        {'title': 'Запланированно', 'tasks': tasks_planned, 'css_class': 'planned'},
        {'title': 'В процессе', 'tasks': tasks_in_progress, 'css_class': 'in-progress'},
        {'title': 'Выполнено', 'tasks': tasks_done, 'css_class': 'done'},
    ]

    context = {
        'task_columns': task_columns,
    }
    return render(request, "polls/tasks_list.html", context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    steps = task.taskstep_set.all()
    return render(request, "polls/task_detail.html", {"task": task, "steps": steps})


def completed_tasks(request):
    tasks_done = Task.objects.filter(is_done=True)
    return render(request, "polls/completed_tasks.html", {"tasks": tasks_done})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('tasks_list')


def create_task(request, status=None):
    TaskForm = get_task_form()  # Импортируем форму здесь
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            posted_status = request.POST.get('initial_status_input')

            if posted_status == 'done':
                task.is_done = True
                task.save()
                TaskStep.objects.create(task=task, text="Задача выполнена при создании", done=True)
            elif posted_status == 'in-progress':
                task.is_done = False
                task.save()
                TaskStep.objects.create(task=task, text="Задача в работе", done=True)
            else:
                task.is_done = False
                task.save()

            return redirect('tasks_list')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'edit_mode': False,
        'initial_status': status
    }
    return render(request, "polls/create_task.html", context)


def edit_task(request, task_id):
    TaskForm = get_task_form()  # Импортируем форму здесь
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, "polls/create_task.html", {'form': form, 'edit_mode': True})


def toggle_task_done(request, task_id):
    """
    Переключает статус выполнения задачи (is_done=True/False).
    """
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.is_done = not task.is_done
        task.save()
        return redirect('task_detail', task_id=task.id)
    return redirect('task_detail', task_id=task.id)


def reset_tasks(request):
    if request.method == 'POST':
        Task.objects.all().delete()
        return redirect('settings')
    return redirect('settings')


@csrf_exempt
def update_task_step(request, step_id):
    if request.method == 'POST':
        step = get_object_or_404(TaskStep, id=step_id)
        try:
            data = json.loads(request.body)
            step.done = data.get('done', step.done)
            step.save()
            return JsonResponse({'status': 'success', 'done': step.done})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)


def about(request):
    return render(request, "polls/about.html")


def settings(request):
    return render(request, "polls/settings.html")
