from django.shortcuts import render
from .models import Topic,Post

def index(request):
    """Home page for Blog."""
    return render(request,'blogs/index.html')
