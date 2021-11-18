from rest_framework import serializers
from .models import Task , movie , Cast,Category,series
from profiels.serializers import UserProfileSerializer

class TaskSerializer(serializers.ModelSerializer):
    """this for post task"""
    # created_by=UserProfileSerializer().fields.get('email')
    class Meta:
        model=Task
        # fields=('name','description','state','created_by')
        fields='__all__'
        # exclude=('created_by',)
        extra_kwargs={'created_by':{'read_only':True}}



class CategSerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=('name',)

class CastSerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=('name',)

class MovieSerializer(serializers.ModelSerializer):
    categories=CategSerializer(many=True)
    cast=CastSerializer(many=True)
    class Meta:
        model=movie
        fields='__all__'
class HelloSerializer(serializers.Serializer):
    """test serialization"""
    name=serializers.CharField(max_length=10)