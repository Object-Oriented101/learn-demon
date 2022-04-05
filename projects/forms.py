from django import forms

from .models import Progress_Block

class Progress_Form(forms.ModelForm):

    class Meta:
        model = Progress_Block
        fields = '__all__' 