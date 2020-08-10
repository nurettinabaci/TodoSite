from django.contrib import admin

# Register your models here.
from .models import Task, EndUser, Tag


class TaskForm(admin.ModelAdmin):
    list_display = ('user','title','date_created')


admin.site.register(Task, TaskForm)
admin.site.register(EndUser)
admin.site.register(Tag)
