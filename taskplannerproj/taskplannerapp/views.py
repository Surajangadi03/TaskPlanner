# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sprint, Task
from django.contrib.auth.models import User
from django.contrib import messages


# Sprint Views
def sprint_list(request):
    "List all sprints"
    sprints = Sprint.objects.all()
    return render(request, 'sprints.html', {'sprints': sprints})

def add_sprint(request):
    "Add a new sprint"
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date') or None
        end_date = request.POST.get('end_date') or None
        Sprint.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            created_by=request.user
        )
        messages.success(request, "Sprint created successfully!")
        return redirect('sprint_list')
    return render(request, 'add_sprint.html')


# Task Views
def task_list(request, sprint_id):
    "List all tasks for a specific sprint"
    sprint = get_object_or_404(Sprint, id=sprint_id)
    tasks = sprint.tasks.all()
    return render(request, 'tasks.html', {'tasks': tasks, 'sprint': sprint})

def add_task(request, sprint_id):
    """Add a task to a specific sprint"""
    sprint = get_object_or_404(Sprint, id=sprint_id)
    users = User.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_type = request.POST.get('task_type')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        assignee_id = request.POST.get('assignee')
        assignee = User.objects.get(id=assignee_id) if assignee_id else None

        Task.objects.create(
            title=title,
            description=description,
            task_type=task_type,
            status=status,
            priority=priority,
            sprint=sprint,
            assignee=assignee
        )
        messages.success(request, "Task added successfully!")
        return redirect('task_list', sprint_id=sprint.id)

    return render(request, 'add_task.html', {'sprint': sprint, 'users': users})


def update_task(request, task_id):
    "Update task status or assignee"
    task = get_object_or_404(Task, id=task_id)
    users = User.objects.all()
    if request.method == 'POST':
        task.status = request.POST.get('status')
        assignee_id = request.POST.get('assignee')
        task.assignee = User.objects.get(id=assignee_id) if assignee_id else None
        task.save()
        messages.success(request, "Task updated successfully!")
        return redirect('task_list', sprint_id=task.sprint.id)
    return render(request, 'update_task.html', {'task': task, 'users': users})


# User-specific Tasks
def user_tasks(request, user_id):
    "Show all tasks assigned to a user"
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.all()
    return render(request, 'tasks.html', {'tasks': tasks, 'sprint': None, 'user_view': user})


# AI Suggestions
def ai_suggestions(request, sprint_id):
    "Simple AI suggestion:Show last 3 tasks of sprint as suggestions for new tasks"
    sprint = get_object_or_404(Sprint, id=sprint_id)
    suggestions = sprint.tasks.order_by('-created_at')[:3]
    return render(request, 'ai_suggestions.html', {'sprint': sprint, 'suggestions': suggestions})





