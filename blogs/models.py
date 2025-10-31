from django.db import models

class Blog(models.Model):
    """An overall blog."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the blog"""
        return self.title

class Post(models.Model):
    """Individual blog post"""
    title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a simple string representing the post."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text}"
