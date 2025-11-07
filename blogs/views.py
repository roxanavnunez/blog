from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic,Post
from .forms import PostForm

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
