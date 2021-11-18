from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework import filters
from rest_framework import permissions
from .models import Task ,movie
from .serializers import TaskSerializer,MovieSerializer

#TODO:AUTH#3
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class CanDeleteTask(BasePermission):

    def has_permission(self, request, view):
        print(f"user group => {request.user.groups}")
        if request.user.groups.filter(name='Can-Delete').exists():
            return True
        return False


class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        """this permission simply work to make sure that
            any user try to access this view (task) must me authenticated
            (logged in)
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """this permission check in 2 steps :
        1- check the request method if from safe methods[get,option] return true
            which allow user to see tasks created by another users but just see
            no edit no delete no actions
        2- if the request method not in safe methods so it mean the request need to
            do some action like edit or delete , now it's turn on to see if the target
            object belongs to the request user or not
        """
        return True if request.method in permissions.SAFE_METHODS else obj.created_by.id==request.user.id


class FetchTask(APIView):
    """test api views"""
    # this help to construct input form as fields type
    serializer_class = TaskSerializer
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','state')
    # permission_classes=[IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    # @permission_classes()
    def get(self, request, format=None):
        """return all tasks"""
        all_date = TaskSerializer(instance=Task.objects.all(),many=True)
        return Response({'Tasks': all_date.data})

    def post(self, request):
        """Handles Post Request to add task"""
        task = TaskSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response({'message': task.data})
        else:
            return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles Update operation"""
        return Response({'method':'put'})

    def delete(self,request,pk=None):
        """it seem to be clear what's it's job"""
        task_id=request.data
        task=Task.objects.get(pk=task_id)
        task.delete()
        return Response({'method':'delete'})

class PutTask(APIView):
    serializer_class = TaskSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'state')
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

class TaskView(ModelViewSet):
    """test view set """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = (UserPermissions,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        print(serializer,'here from perform create')

    class SubTaskView(ViewSet):
        def list(self, request):
            """list all objects"""
            data=Task.objects.all()
            all_date = TaskSerializer(instance=data,many=True)
            return Response({'message from sub task': all_date.data})


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) #TODO:AUTH#4
def get_tasks(request):
        print(request.user)
        all_date = MovieSerializer(instance=movie.objects.all(),many=True)
        return Response({'token': all_date.data})


@api_view(['POST'])
def add_tasks(request):
        task=TaskSerializer(data=request.data)
        if task.is_valid():
            task.save()
        all_date = TaskSerializer(instance=Task.objects.all(),many=True)
        return Response({'Tasks': all_date.data})

@api_view(['PUT','PATCH'])
def update_tasks(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='PUT':
        result=TaskSerializer(instance=task,data=request.data )
    elif request.method=='PATCH':
        result=TaskSerializer(instance=task,data=request.data ,partial=True)
    if result.is_valid():
        result.save()
    return Response({'task':result.data})

@api_view(['POST'])
def add_movie(request):
    movie=MovieSerializer(data=request.data)
    if movie.is_valid():
        movie.save()
        return Response({'message':movie.data})
    else:
        return Response({'message':status.HTTP_400_BAD_REQUEST})

@api_view(['DELETE'])
@permission_classes([CanDeleteTask])
def delete_task(request,pk):
    task=Task.objects.filter(pk=pk)
    task.delete()
    return Response({"message":TaskSerializer(instance=Task.objects.all(),many=True).data})