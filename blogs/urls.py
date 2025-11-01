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
]