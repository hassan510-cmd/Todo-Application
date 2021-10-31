from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """this for post task"""
    class Meta:
        model=Task
        fields='__all__'


class HelloSerializer(serializers.Serializer):
    """test serialization"""
    name=serializers.CharField(max_length=10)