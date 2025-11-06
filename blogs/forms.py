from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'size': 50}),
            'text': forms.Textarea(attrs={'rows':10, 'cols': 50}),
        }