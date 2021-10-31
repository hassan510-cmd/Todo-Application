from django.db import models
import json


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    state = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'description': self.description
            , 'state': self.state
        })
    @staticmethod
    def get_all_tasks():
        """
        this method get all tasks object then return list with them
        [
        {"id": 1, "name": "task1", "description": "desc1", "state": 0},
         {"id": 2, "name": "Veda Hayes", "description": "Eos eos voluptas id vel quibusdam odio aut ducimus, sunt fugit, irure magni sed mollitia doloremque .", "state": 0},
         {"id": 3, "name": "Maryam Vincent", "description": "Dolorem rem in ea tempor molestiae irure molestiae dolores error consequat. Est est eiusmod a tempor.", "state": 0},
         {"id": 4, "name": "Xanthus Bowers", "description": "Itaque accusantium consequatur dolore omnis amet, iste aliquid laborum. In ut dolore voluptatibus qu.", "state": 0}
         ]

        """
        all_tasks = Task.objects.all()
        list_of_tasks_objects = [{'id':task.id,'name':task.name,'description':task.description,'state':task.state} for task in all_tasks]
        return list_of_tasks_objects


# from todo.models import Task
#
# all_tasks = Task.objects.all()
# [type(json.dump(task)) for task in all_tasks]
# import json