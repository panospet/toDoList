from rest_framework import serializers
from toDoList.models import Task

class TaskSerializer(serializers.ModelSerializer):
	'''
	Serializes task model for json API.
	'''
	class Meta:
		model = Task