from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class StudyMaterial(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='study_materials')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='study_materials/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class PreviousYearQuestion(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='previous_year_questions/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default="No subject")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(default='', blank=True)

    def __str__(self):
        return self.title

# New Models for Forum
class Forum(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    forum = models.ForeignKey(Forum, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.created_by} on {self.forum}'
