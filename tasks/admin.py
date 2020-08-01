from django.contrib import admin

# Register your models here.
from .models import Task, EndUser, Tag

admin.site.register(Task)
admin.site.register(EndUser)
admin.site.register(Tag)
