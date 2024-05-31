# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Post, Subject, StudyMaterial, PreviousYearQuestion, Announcement, Reminder, Forum, Comment
from .forms import ReminderForm, ForumForm, CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    # Query for subjects
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(name__icontains=query)
    else:
        subjects = Subject.objects.all()

    # Query for announcements
    announcements = Announcement.objects.all()

    # Handle reminder form submission
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = ReminderForm()

    # Query for reminders
    reminders = Reminder.objects.all()

    return render(request, 'blog/home.html', {
        'subjects': subjects,
        'announcements': announcements,
        'form': form,
        'reminders': reminders
    })

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def help(request):
    return render(request, 'blog/help.html', {'title': 'Help'})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    study_materials = subject.study_materials.all()
    previous_questions = subject.previousyearquestion_set.all()
    return render(request, 'blog/subject_detail.html', {
        'subject': subject,
        'study_materials': study_materials,
        'previous_questions': previous_questions
    })

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')
        else:
            return HttpResponse('Invalid login credentials')
    else:
        return render(request, 'blog/login.html')


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'blog/forum_list.html', {'forums': forums})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    comments = forum.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.forum = forum
            new_comment.created_by = request.user
            new_comment.save()
            return redirect('forum-detail', forum_id=forum.id)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/forum_detail.html', {
        'forum': forum,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.created_by = request.user
            new_forum.save()
            return redirect('forum-detail', forum_id=new_forum.id)
    else:
        form = ForumForm()
    
    return render(request, 'blog/create_forum.html', {'form': form})


def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    comments = forum.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.forum = forum
            new_comment.created_by = request.user
            new_comment.save()
            return redirect('forum-detail', forum_id=forum.id)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/forum_detail.html', {
        'forum': forum,
        'comments': comments,
        'comment_form': comment_form
    })
