from django.contrib import admin
from .models import Task , Cast ,Category,movie,series
# Register your models here.
admin.site.register(Task)
admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(movie)
admin.site.register(series)