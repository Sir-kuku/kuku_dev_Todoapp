from django.shortcuts import (
    render, redirect, get_object_or_404
    )
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
#model
from .models import Task
# Create your views here.

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'



# function based views
@login_required
def task_list(request):
    tasks = Task.objects.all() # all tasks
    tasks = Task.objects.filter(user=request.user).order_by('due_date') # filtered tasks
    return render(request, 
                  'task_list.html', 
                  {'tasks': tasks})
@login_required
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task,
                             pk=pk)
    return render(request,
                  'task_detail.html',
                  {'task':task})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html',
                   {'form': form})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')
    
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,
                  'task_confirm_delete.html',
                  {'task': task})
