from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        'author': 'Harsha Varma',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'May 15th, 2003'
    },
      
    {
        'author': 'Varma',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'May 16th, 2003'
    }
]

def home(request):
    context = {
        'posts': posts 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About' })