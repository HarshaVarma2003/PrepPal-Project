# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default="No subject")  # Add a default value here
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(default='', blank=True)
    
    def __str__(self):
        return self.title
