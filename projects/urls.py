from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<project_id>', views.project, name='project_access'),

    path('project-addition/', views.form_project, name='add-project'),
    path('scoping-block-addition/<int:project_id>', views.form_scoping_block, name='add-scope-block'),
    path('high-level-task-addition/<int:project_id>', views.create_high_level_task, name='add-task'),
    path('progress-block-addition/<int:project_id>', views.form_progress_block, name='add-progress-block'),

    path('update-project/<project_id>', views.update_project, name='update-project'),
    path('scoping-block-update/<project_id>/<scoping_block_id>', views.update_scoping_block, name='update-scoping'),
    path('update-task/<project_id>/<high_level_task_id>', views.update_high_level_task, name='update-task'),
    path('progress-block-update/<project_id>/<progress_block_id>', views.update_progress_block, name='update-progress'),

    path('project-delete/<project_id>', views.delete_project, name='delete-project'),
    path('scoping-block-delete/<project_id>/<scoping_block_id>', views.delete_scoping_block, name='delete-scoping'),
    path('high-level-task-delete/<project_id>/<high_level_task_id>', views.delete_high_level_task, name='delete-task'),
    path('progress-block-delete/<project_id>/<progress_block_id>', views.delete_progress_block, name='delete-progress'),
]
