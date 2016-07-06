from django.shortcuts import render
from rest_framework import viewsets
from toDoList.models import Task
from toDoList.serializers import TaskSerializer
from django.contrib.auth.decorators import login_required

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

@login_required
def index(request):
	return render(request, 'toDoList/index.html')
