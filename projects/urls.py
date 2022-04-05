from django import views
from django.urls import path


from projects.views import * 


urlpatterns = [
    path('', index),
]
