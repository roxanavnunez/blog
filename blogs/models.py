from django.db import models

class Topic(models.Model):
    """An overall blog."""
    topic = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the blog"""
        return self.topic

class Post(models.Model):
    """Individual blog post"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a simple string representing the post."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        return f"{self.title}"