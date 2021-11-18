from django.urls import path
from django.conf.urls import url , include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('list',views.TaskView,basename='list')
router.register('list2',views.TaskView.SubTaskView,basename='list2')
#todo
urlpatterns=[
    path('hello-view/',views.FetchTask.as_view()),
    path('hello-view2/task_id/',views.PutTask.as_view()),
    path('get/',views.get_tasks),
    path('add/',views.add_tasks),
    path('edit/<int:pk>',views.update_tasks),
    path('add-movie/',views.add_movie),
    path('remove/<int:pk>',views.delete_task),
    url('',include(router.urls))
    # path('list/',views.TaskView.as_view()),
    # url('hello-view2/',views.PutTask.as_view()),
]