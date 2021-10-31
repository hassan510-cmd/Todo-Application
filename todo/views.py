from django.shortcuts import render
from dns.update import Update
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from . import serializers
from rest_framework.viewsets import ViewSet

# Create your views here.

class FetchTask(APIView):
    """test api views"""
    # this help to construct input form as fields type
    serializer_class = serializers.TaskSerializer

    def get(self, request, format=None):
        """return all tasks"""
        all_date = Task.get_all_tasks()
        return Response({'Tasks': all_date})

    def post(self, request):
        """Handles Post Request to add task"""
        task = serializers.TaskSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response({'message': task.data})
        else:
            return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles Update operation"""
        return Response({'method':'put'})

    # def patch(self,request,pk=None):
    #     """Handle Partial update process"""
    #     task_id=request.data
    #     task=Task.objects.get(pk=task_id)
    #     new_state=0 if task.state else 1
    #     updated_task=serializers.TaskSerializer(instance=task,data={'state':new_state},partial=True)
    #     updated_task.save() if updated_task.is_valid() else print('not valid')
    #     return Response({'message':updated_task.data})

    def delete(self,request,pk=None):
        """it seem to be clear what's it's job"""
        task_id=request.data
        task=Task.objects.get(pk=task_id)
        task.delete()
        return Response({'method':'delete'})

class PutTask(APIView):
    serializer_class = serializers.TaskSerializer
    def get(self, request, format=None):
        """return all tasks"""
        all_date = Task.get_all_tasks()
        # print(self.kwargs.get('task_id',None))
        print(request.query_params["id"])
        # print(task_id)
        return Response({'Tasks': all_date})
    def put(self,request,pk=None):
        """Handles Update operation"""
        return Response({'method':'putx'})

class TaskView(ViewSet):
    """test view set """
    serializer_class = serializers.TaskSerializer
    def list(self,request):
        """list all objects"""
        all_date = Task.get_all_tasks()
        return Response({'message':all_date})

    def create(self,request):
        task = serializers.TaskSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response({'message': task.data})
        else:
            return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handle get object by id"""
        print(pk)
        task=Task.objects.get(id=pk)
        task_result={'id':task.id,'name':task.name,'description': task.description,'state':task.state}

        return Response({"task":task_result})

    def update(self,request, pk=None):
        """Handles updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle partial update"""
        task=Task.objects.get(pk=pk)
        new_state=0 if task.state else 1
        updated_task=serializers.TaskSerializer(instance=task,data={'state':new_state},partial=True)
        updated_task.save() if updated_task.is_valid() else print('not valid')
        return Response({'message':updated_task.data})
        # return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """Handle delete object"""
        task=Task.objects.get(pk=pk)
        task.delete()
        delete_result={'id':task.id,'name':task.name,'description': task.description,'state':task.state}
        return Response({'message': delete_result})

