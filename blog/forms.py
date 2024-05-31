# blog/forms.py

from django import forms
from .models import Forum, Comment, Reminder

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title']

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ['content', 'file']
        
class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['date', 'description']
