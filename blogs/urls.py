"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Page to show all topics
    path('topics/', views.topics, name='topics'),
    # Page to show individual topic 
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page to show the content of a post
    path('post/<int:post_id>', views.post, name='post'),
    
    # Page to edit a post
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # Page to edit a topic
    path('topic/<int:topic_id>/edit/', views.edit_topic, name='edit_topic')

]