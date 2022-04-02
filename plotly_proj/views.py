from django.shortcuts import render
from projects.models import Progress_Block, Project
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import random


def index(request):

    #Line Graph Code
    progress_blocks = Progress_Block.objects.all()
    parsed_progress_blocks = [
        {
        'Time': i.time,
        'Date': i.date,
        'Description': i.description
        } for i in progress_blocks
    ] 

    df_progress_block = pd.DataFrame(parsed_progress_blocks)
    line_fig = px.line(df_progress_block, x = "Date", y = "Time", title = "Daily Progress")
    line_plot = plot(line_fig, output_type="div")

    #Project Details passback
    project_retrieval = Project.objects.all() #ERROR CHECK IF EMPTY
    project_details = project_retrieval[0]
    

    context = {'line_plot': line_plot, 'project_details': project_details}
    return render(request, 'index.html', context)
