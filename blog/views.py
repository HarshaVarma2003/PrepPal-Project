# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts}) 

def about(request):
    return render(request, 'blog/about.html', {'title':'About' })

def contact(request):
    return render(request, 'blog/contact.html', {'title':'Contact' })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

#login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')  # Redirect to home page after successful login
        else:
            return HttpResponse('Invalid login credentials')  # Display error message
    else:
        return render(request, 'blog/login.html')

