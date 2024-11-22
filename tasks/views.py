from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')  # Default to empty string if not provided
        description = request.POST.get('description', '')  
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_form.html')

@login_required
def task_edit(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('task_list')

def homepage(request):
    return render(request, 'homepage.html')
