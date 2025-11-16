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
    path('topic/<int:topic_id>/edit/', views.edit_topic, name='edit_topic'),

    # Page to add a topic
    path('topics/new', views.new_topic, name='new_topic'),
    # Page to add a post
    path('topics/<int:topic_id>/new-post', views.new_post, name='new_post'),

]