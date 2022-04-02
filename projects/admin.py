from django.contrib import admin
from .models import Progress_Block, Project, Investor

# Register your models here.
admin.site.register(Project)
admin.site.register(Investor)
admin.site.register(Progress_Block)