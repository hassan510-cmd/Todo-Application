from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from . import serializers


# Create your views here.

class FetchTask(APIView):
    """test api views"""

    serializer_class = serializers.TaskSerializer

    def get(self, request, formate=None):
        """return all tasks"""
        all_date = Task.get_all_tasks()
        return Response({'Tasks': all_date})

    def post(self, request):
        task = serializers.TaskSerializer(data=request.data)
        if task.is_valid():

            task.save()
            # result = {
            #     'id': task.data.get('id'),
            #     'name': task.name,
            #     'description': task.description,
            #     'state': task.state
            # }
            # print(task.data)
            return Response({'message': task.data})
        else:
            return Response(s1.errors, status=status.HTTP_400_BAD_REQUEST)
