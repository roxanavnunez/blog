from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic,Post
from .forms import PostForm, TopicForm

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
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.post_set.order_by('-date_last_modified')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'blogs/topic.html', context)

def post(request, post_id):
    """Show the content of each post """
    post_object = get_object_or_404(Post, id=post_id)
    context = {'post': post_object}
    return render(request,'blogs/post.html', context)

def edit_post(request, post_id):
    """Edit an existing post"""
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

def edit_topic(request, topic_id):
    """Edit an existing topic"""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('blogs:topic', topic_id=topic.id)
    else:
        form = TopicForm(instance=topic)
    
    context = {'form': form, 'topic': topic}
    return render(request, 'blogs/edit_topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:topics')
    else:
        form = TopicForm()
    
    context = {'form':form}
    return render(request, 'blogs/new_topic.html', context)

def new_post(request, topic_id):
    """Add a new post"""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.save()
            return redirect('blogs:topic', topic_id=topic.id)
    else:
        form = PostForm()
    
    context = {'form':form, 'topic':topic}
    return render(request, 'blogs/new_post.html', context)

    
