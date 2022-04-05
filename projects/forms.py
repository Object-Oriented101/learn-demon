from django import forms

from .models import Progress_Block, Scoping_Block

class Progress_Form(forms.ModelForm):

    class Meta:
        model = Progress_Block
        fields = '__all__' 

class Scoping_Form(forms.ModelForm):

    class Meta:
        model = Scoping_Block 
        fields = '__all__' 