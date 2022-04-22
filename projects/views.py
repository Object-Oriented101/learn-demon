import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from .forms import Project_Form, High_Level_Task_Form, Progress_Form, Scoping_Form 

from projects.models import Progress_Block, Scoping_Block, Project, High_Level_Task
import pandas as pd
from plotly.offline import plot
import plotly.express as px

#Clean up the little things
#   -Subtasks filtered by scope
# Deployment...
# Login for different users...
# Future Tasks
#   -UI Revamp (Layout, Forms, Back buttons)
#   -Autofill date for today and add a calendar

def project(request, project_id):

    #project_id = 1
    #Line Graph
    progress_blocks = Progress_Block.objects.filter(project_id=project_id)


    parsed_progress_blocks = [
        {
        'Hours': i.hours,
        'Date': i.date,
        'Description': i.description
        } for i in progress_blocks
    ] 

    parsed_progress_blocks = sorted(parsed_progress_blocks, key=lambda p: p['Date'], reverse=False)

    df_progress_block = pd.DataFrame(parsed_progress_blocks)
    line_fig = 0;
    if len(df_progress_block) != 0:
        line_fig = px.line(df_progress_block, x = "Date", y = "Hours", text="Date", template="plotly_white", width=900, height=400)
    else:
        line_fig = px.line(df_progress_block,  template="plotly_white", width=900, height=400)

    line_fig.update_traces(textposition="bottom right")
    line_plot = plot(line_fig, output_type="div")

    #Project Details passback
    project_retrieval = Project.objects.filter(pk=project_id) #ERROR CHECK IF EMPTY
    project_details = project_retrieval[0]

    #Scoping Details passback
    scoping_blocks = Scoping_Block.objects.filter(project_id=project_id) #ERROR CHECK IF EMPTY

    #High-Level Tasks Details passback
    high_level_task_list = High_Level_Task.objects.filter(project_id=project_id)
    

    context = {'line_plot': line_plot, 'project_details': project_details, 'progress_blocks': progress_blocks, 
    'scoping_blocks' : scoping_blocks, 'high_level_tasks': high_level_task_list } 
    return render(request, 'project_view.html', context)

def index(request):
    project_retrieval = Project.objects.all() 

    context = {'projects': project_retrieval}
    return render(request, 'index.html', context)

#-----------------------CREATE-------------------------
def form_project(request):
    if request.method == 'POST':
        form = Project_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Project was added!'))
            return redirect('home')
    form = Project_Form()
    return render(request, 'form_project.html', {'form': form})

def form_scoping_block(request, project_id):
    if request.method == 'POST':
        #project = Project.objects.get(pk=project_id)
        form = Scoping_Form(request.POST)
        if form.is_valid():
            #form.instance.project = project
            form.save()
            messages.success(request, ('Scoping Block was added!'))
            return HttpResponseRedirect(reverse('project', args=[project_id]))
    
    form = Scoping_Form()
    return render(request, 'form_scoping.html', {'form': form})

def create_high_level_task(request, project_id):
    #scope_block = scope_block.objects.get(pk=scope_block_id)
    #form = High_Level_Task_Form(request.POST or None, instance=scope_block)
    if request.method == 'POST':
        form = High_Level_Task_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('High Level Task was added!'))
            return HttpResponseRedirect(reverse('project', args=[project_id]))
    
    form = High_Level_Task_Form()
    return render(request, 'form_high_leveL_task.html', {'form': form})

def form_progress_block(request, project_id):
    if request.method == 'POST':
        form = Progress_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Progress block was added!'))
            return HttpResponseRedirect(reverse('project', args=[project_id]))
    form = Progress_Form()
    return render(request, 'form_progress_log.html', {'form': form})

#-----------------------UPDATE-------------------------
def update_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = Project_Form(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        messages.success(request, ('Project was updated!'))
        return HttpResponseRedirect(reverse('project', args=[project_id]))
    return render(request, 'form_project_update.html', {'form': form})

def update_scoping_block(request, project_id, scoping_block_id):
    scoping_block = Scoping_Block.objects.get(pk=scoping_block_id)
    form = Scoping_Form(request.POST or None, instance=scoping_block)
    if form.is_valid():
        form.save()
        messages.success(request, ('Scoping Block was updated!'))
        return HttpResponseRedirect(reverse('project', args=[project_id]))
    return render(request,'form_progress_update.html', {'scoping_block': scoping_block, 'form': form})

def update_high_level_task(request, project_id, high_level_task_id):
    task = High_Level_Task.objects.get(pk=high_level_task_id)
    form = High_Level_Task_Form(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, ('High Level Task was updated!'))
        return HttpResponseRedirect(reverse('project', args=[project_id]))
    return render(request, 'form_high_leveL_task.html', {'form': form})

def update_progress_block(request, project_id, progress_block_id):
    progress_block = Progress_Block.objects.get(pk=progress_block_id)
    form = Progress_Form(request.POST or None, instance=progress_block)
    if form.is_valid():
        form.save()
        messages.success(request, ('Progress Block was updated!'))
        return HttpResponseRedirect(reverse('project', args=[project_id]))
    return render(request,'form_progress_update.html', {'progress_block': progress_block, 'form': form})



#-----------------------DELETE-------------------------
def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('home')

def delete_scoping_block(request, project_id, scoping_block_id):
    scoping_block = Scoping_Block.objects.get(pk=scoping_block_id)
    scoping_block.delete()
    return HttpResponseRedirect(reverse('project', args=[project_id]))

def delete_high_level_task(request, project_id, high_level_task_id):
    high_level_task = High_Level_Task.objects.get(pk=high_level_task_id)
    high_level_task.delete()
    return HttpResponseRedirect(reverse('project', args=[project_id]))

def delete_progress_block(request, project_id, progress_block_id):
    progress_block = Progress_Block.objects.get(pk=progress_block_id)
    progress_block.delete()
    return HttpResponseRedirect(reverse('project', args=[project_id]))
