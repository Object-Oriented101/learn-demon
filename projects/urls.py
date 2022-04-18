from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<project_id>', views.project, name='home'),
    path('progress-block-addition', views.form_progress_block),
    path('scoping-block-addition', views.form_scoping_block),
    path('high-level-task/', views.create_high_level_task, name='new-task'),
    path('update-task/<high_level_task_id>', views.update_high_level_task, name='update-task'),

    path('progress-block-update/<progress_block_id>', views.update_progress_block, name='update-progress'),
    path('scoping-block-update/<scoping_block_id>', views.update_scoping_block, name='update-scoping'),

    path('progress-block-delete/<progress_block_id>', views.delete_progress_block, name='delete-progress'),
    path('scoping-block-delete/<scoping_block_id>', views.delete_scoping_block, name='delete-scoping'),
]
