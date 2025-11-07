from django import forms
from .models import Post, Topic

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'size': 50}),
            'text': forms.Textarea(attrs={'rows':10, 'cols': 50}),
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        widgets = {
            'topic': forms.TextInput(attrs={'size': 50})
        } 