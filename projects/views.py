from django.shortcuts import redirect, render

from .forms import High_Level_Task_Form, Progress_Form, Scoping_Form 

from projects.models import Progress_Block, Scoping_Block, Project, High_Level_Task
import pandas as pd
from plotly.offline import plot
import plotly.express as px

#Add subtasks for the scope and figure out how to integrate it with progress blocks
#Create a view for multiple projects``
#BOOT STRAP TIME!

def index(request):

    #Line Graph 
    progress_blocks = Progress_Block.objects.all()

    parsed_progress_blocks = [
        {
        'Hours': i.hours,
        'Date': i.date,
        'Description': i.description
        } for i in progress_blocks
    ] 

    df_progress_block = pd.DataFrame(parsed_progress_blocks)
    line_fig = px.line(df_progress_block, x = "Date", y = "Hours", title = "Daily Progress", text="Date", width=800, height=400)
    line_fig.update_traces(textposition="bottom right")
    line_plot = plot(line_fig, output_type="div")

    #Project Details passback
    project_retrieval = Project.objects.all() #ERROR CHECK IF EMPTY
    project_details = project_retrieval[0]

    #Scoping Details passback
    scoping_blocks = Scoping_Block.objects.all() #ERROR CHECK IF EMPTY

    #High-Level Tasks Details passback
    high_level_task_list = High_Level_Task.objects.all()
    

    context = {'line_plot': line_plot, 'project_details': project_details, 'progress_blocks': progress_blocks, 
    'scoping_blocks' : scoping_blocks, 'high_level_tasks': high_level_task_list } 
    return render(request, 'index.html', context)

#Form to add a new progress to scop
def form_progress_block(request):
    if request.method == 'POST':
        form = Progress_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Progress_Form()
    return render(request, 'form_progress_log.html', {'form': form})

#Form to add a new scope block to a project
def form_scoping_block(request):
    if request.method == 'POST':
        form = Scoping_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = Scoping_Form()
    return render(request, 'form_scoping.html', {'form': form})

def form_high_level_task(request):
    if request.method == 'POST':
        form = High_Level_Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = High_Level_Task_Form()
    return render(request, 'form_high_leveL_task.html', {'form': form})

def update_progress_block(request, progress_block_id):
    progress_block = Progress_Block.objects.get(pk=progress_block_id)
    form = Progress_Form(request.POST or None, instance=progress_block)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'form_progress_update.html', {'progress_block': progress_block, 'form': form})

def update_scoping_block(request, scoping_block_id):
    scoping_block = Scoping_Block.objects.get(pk=scoping_block_id)
    form = Scoping_Form(request.POST or None, instance=scoping_block)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'form_progress_update.html', {'scoping_block': scoping_block, 'form': form})

def delete_progress_block(request, progress_block_id):
    progress_block = Progress_Block.objects.get(pk=progress_block_id)
    progress_block.delete()
    return redirect('home')

def delete_scoping_block(request, scoping_block_id):
    scoping_block = Scoping_Block.objects.get(pk=scoping_block_id)
    scoping_block.delete()
    return redirect('home')