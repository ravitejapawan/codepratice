from django import forms
from .models import TextEntry

class TextEntryForm(forms.ModelForm):
    class Meta:
        model = TextEntry
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Enter your text...',
                'style': 'white-space: pre-wrap;'
            })
        }
