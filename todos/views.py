from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    posted_task=request.POST['task']
    Task.objects.create(task=posted_task)
    return redirect("home")
