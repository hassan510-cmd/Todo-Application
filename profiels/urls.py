from django.conf.urls import url , include
from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import UserProfileViewSet

#TODO:AUTH#5
from rest_framework.authtoken.views import obtain_auth_token
from .views import  logout, LoginViewSet, signup
router=DefaultRouter()
# router.register('profiles',UserProfileViewSet,basename='profiles')
router.register('login2',LoginViewSet,basename='login2')
urlpatterns=[
    url('',include(router.urls)),
    path('login/',obtain_auth_token),
    path('logout/',logout),
    path('signup/',signup)
]