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

def topic(request, topic_id):
    """Show posts for each topic"""
    topic = Topic.objects.get(id=topic_id)
    titles = topic.title_set.order_by('-date_last_modified')
    context = {'topic': topic, 'titles': titles}
    return render(request, 'blogs/topic.html', context)