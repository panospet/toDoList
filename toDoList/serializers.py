from rest_framework import serializers
from toDoList.models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task