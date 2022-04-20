from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<project_id>', views.project, name='project'),

    path('project-addition/', views.form_project, name='add-project'),
    path('scoping-block-addition/<project_id>', views.form_scoping_block, name='add-scope-block'),
    path('high-level-task-addition/<project_id>', views.create_high_level_task, name='add-task'),
    path('progress-block-addition/<project_id>', views.form_progress_block, name='add-progress-block'),

    path('update-project/<project_id>', views.update_project, name='update-project'),
    path('scoping-block-update/<scoping_block_id>', views.update_scoping_block, name='update-scoping'),
    path('update-task/<high_level_task_id>', views.update_high_level_task, name='update-task'),
    path('progress-block-update/<progress_block_id>', views.update_progress_block, name='update-progress'),

    path('progress-block-delete/<progress_block_id>', views.delete_progress_block, name='delete-progress'),
    path('scoping-block-delete/<scoping_block_id>', views.delete_scoping_block, name='delete-scoping'),
    path('project-delete/<project_id>', views.delete_project, name='delete-project'),
]
