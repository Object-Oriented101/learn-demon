from django import forms

from .models import Project, Progress_Block, Scoping_Block, High_Level_Task


class Project_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__' 

class Progress_Form(forms.ModelForm):

    class Meta:
        model = Progress_Block
        fields = '__all__' 

class Scoping_Form(forms.ModelForm):

    class Meta:
        model = Scoping_Block 
        fields = '__all__' 
        #exclude = ('project',)

class High_Level_Task_Form(forms.ModelForm):

    class Meta:
        model = High_Level_Task 
        fields = '__all__' 