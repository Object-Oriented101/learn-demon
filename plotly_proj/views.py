from django.shortcuts import render
from projects.models import Progress_Block, Project
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import random


def index(request):

    #Line Graph Code
    progress_blocks = Progress_Block.objects.all()
    progress_0 = progress_blocks[len(progress_blocks) - 1]
    progress_1 = progress_blocks[len(progress_blocks) - 2]
    progress_2 = progress_blocks[len(progress_blocks) - 3]

    parsed_progress_blocks = [
        {
        'Hours': i.hours,
        'Date': i.date,
        'Description': i.description
        } for i in progress_blocks
    ] 

    df_progress_block = pd.DataFrame(parsed_progress_blocks)
    line_fig = px.line(df_progress_block, x = "Date", y = "Hours", title = "Daily Progress")

    line_plot = plot(line_fig, output_type="div")

    #Project Details passback
    project_retrieval = Project.objects.all() #ERROR CHECK IF EMPTY
    project_details = project_retrieval[0]
    

    context = {'line_plot': line_plot, 'project_details': project_details, 'progress_0': progress_0, 'progress_1': progress_1, 'progress_2': progress_2, 'progress_details': progress_blocks}
    return render(request, 'index.html', context)
