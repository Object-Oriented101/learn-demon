from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('progress-block-addition', views.form_progress_block),
    path('scoping-block-addition', views.form_scoping_block),
]
