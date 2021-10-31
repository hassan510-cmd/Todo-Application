from django.urls import path
from django.conf.urls import url
from . import views

#todo
urlpatterns=[
    url('hello-view/',views.FetchTask.as_view()),
]