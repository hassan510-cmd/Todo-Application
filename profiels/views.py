from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from rest_framework.authentication import BasicAuthentication

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import status

from .serializers import UserProfileSerializer


User=get_user_model()
@api_view(['POST'])
def signup(request):
    user = UserProfileSerializer(data=request.data)
    if user.is_valid():
        user.save()
        created=User.objects.get(email=user.data['email'])
        print(user.validated_data)
        token=Token.objects.create(user=created)
        return Response({'message':token.key})
    return Response({'message':user.errors})


@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "logged out"})

class LoginViewSet(ViewSet):
    serializer_class = AuthTokenSerializer
    def create(self, request):
        username=request.data['username']
        password=request.data['password']
        user = authenticate(email=username,password=password)
        if user:
            token=Token.objects.create(user=user)
            return Response({'token':token.key})
        print(username,password)
        return Response({"ObtainAuthToken().post(request)": "7584"})
# from .models import UserProfile
# from .serializers import UserProfileSerializer
# Create your views here.
# class UserProfileViewSet(ModelViewSet):
#     serializer_class=UserProfileSerializer
#     queryset=UserProfile.objects.all()
