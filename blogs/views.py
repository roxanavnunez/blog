from django.shortcuts import render
from .models import Topic,Post

def index(request):
    """Home page for Blog."""
    return render(request,'blogs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_last_modified')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)
