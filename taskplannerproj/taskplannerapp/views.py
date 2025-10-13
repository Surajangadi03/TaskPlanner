# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sprint, Task
from django.contrib.auth.models import User
from django.contrib import messages


# Sprint Views
def sprint_list(request):
    """List all sprints"""
    sprints = Sprint.objects.all()
    return render(request, 'planner/sprints.html', {'sprints': sprints})

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
    return render(request, 'planner/add_sprint.html')


# Task Views
def task_list(request, sprint_id):
    "List all tasks for a specific sprint"
    sprint = get_object_or_404(Sprint, id=sprint_id)
    tasks = sprint.tasks.all()
    return render(request, 'planner/tasks.html', {'tasks': tasks, 'sprint': sprint})





