from django.shortcuts import render
from projects.models import Progress_Block,Project, Investor
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import random


def index(request):
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

    #Database Scatter Plot
    investors = Investor.objects.all()
    investors_data = [
        {
            'Name': x.name,
            'Age': x.age,
            'College': x.college,
            'Net_Worth': x.net_worth

        } for x in investors
    ]
    df_investors_data = pd.DataFrame(investors_data)
    scatter_fig= px.scatter(df_investors_data, x = "Age", y = "Net_Worth", text = "Name")
    scatter_fig.update_traces(textposition='top center')
    scatter_plot = plot(scatter_fig, output_type="div")


    #Bar Graph
    qs = Project.objects.all()
    projects_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.end_date,
            'Responsible': x.responsible.username
        } for x in qs
    ]

    df = pd.DataFrame(projects_data)

    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )

    fig.update_yaxes(autorange="reversed") 
    gantt_plot = plot(fig, output_type="div")

    #Box Plot
    random.seed(10)
    randomlist = []
    for i in range(0,100):
        n = random.randint(1,100)
        randomlist.append(n)
    
    box_plot = plot(px.box(randomlist), output_type="div")

    context = {'line_plot': line_plot, 'gantt_plot': gantt_plot, 'scatter_plot': scatter_plot, 'box_plot': box_plot}
    return render(request, 'index.html', context)
