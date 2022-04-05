from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('progress-block-addition', views.form_progress_block)
]
