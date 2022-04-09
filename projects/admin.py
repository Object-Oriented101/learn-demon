from django.contrib import admin
from .models import High_Level_Task, Progress_Block, Scoping_Block, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Progress_Block)
admin.site.register(Scoping_Block)
admin.site.register(High_Level_Task)