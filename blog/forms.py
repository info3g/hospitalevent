from django import forms
from .models import blogpost
from ckeditor.widgets import CKEditorWidget

class MyForm(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = ['title', 'body','link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.CharField(widget=CKEditorWidget()),
            'link': forms.TextInput(attrs={'class': 'form-control'}),

        }