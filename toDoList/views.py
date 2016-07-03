from django.shortcuts import render
from rest_framework import viewsets
from toDoList.models import Task
from toDoList.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

def index(request):
	return render(request, 'toDoList/index.html')
