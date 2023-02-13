from django import forms
from .models import Write

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['date','title', 'content']
        widgets = {
            'date':forms.NumberInput(
                attrs={
                    'type' :'date',
                    'class': 'form-control',
                    'style' : 'width:25%; height:30px;',
                    'placeholder': 'today date'
                    }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'title',
                    'style' : 'width:100%; height:50px;'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'what happened to your day',
                    'style' : 'width:100%; height:500px'
                }
            )
        }