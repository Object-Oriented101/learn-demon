from django.contrib import admin
from .models import Progress_Block, Scoping_Block, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Progress_Block)
admin.site.register(Scoping_Block)