from django.shortcuts import render
from rest_framework import viewsets
from toDoList.models import Task
from toDoList.serializers import TaskSerializer
from django.contrib.auth.decorators import login_required

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def index(request):
	'''
	Index view
	'''
	return render(request, 'toDoList/index.html')