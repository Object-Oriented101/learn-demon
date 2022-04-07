from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('progress-block-addition', views.form_progress_block),
    path('scoping-block-addition', views.form_scoping_block),
    path('progress-block-update/<progress_block_id>', views.update_progress_block, name='update-progress'),
    path('scoping-block-update/<scoping_block_id>', views.update_scoping_block, name='update-scoping'),
]
