from django.db import models
import json
from profiels.models import UserProfile
from django.conf import settings

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    state = models.IntegerField(default=0)
    created_by=models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
class SharedInfo(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField(max_length=1000)
    release_date=models.DateField()
    categories=models.ManyToManyField(to=Category)
    cast=models.ManyToManyField(to=Cast)
    poster_image=models.ImageField(upload_to='movie/posters')

    class Meta:
        abstract = True

class movie(SharedInfo):
    pass

class series(SharedInfo):
    pass
