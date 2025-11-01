from django.contrib import admin
from .models import Topic, Post

class PostInLine(admin.TabularInline):
    """Post should be editaable inline"""
    model = Post
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    """Personalized setting for Topic"""
    inlines = [PostInLine]

admin.site.register(Topic, TopicAdmin)


