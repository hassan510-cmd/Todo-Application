from django.urls import path
from django.conf.urls import url , include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('list',views.TaskView,basename='list')
#todo
urlpatterns=[
    url('hello-view/',views.FetchTask.as_view()),
    url('hello-view2/task_id/',views.PutTask.as_view()),
    # url('list/',views.TaskView.as_view()),
    url('',include(router.urls))
    # url('hello-view2/',views.PutTask.as_view()),
]