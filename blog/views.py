from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Post, Subject, StudyMaterial, PreviousYearQuestion, Announcement

def home(request):
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(name__icontains=query)
    else:
        subjects = Subject.objects.all()
    # Assuming you have a queryset for announcements as well
    announcements = Announcement.objects.all()
    return render(request, 'blog/home.html', {'subjects': subjects, 'announcements': announcements})

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
    previous_questions = subject.previousyearquestion_set.all()  # Fetch previous year questions related to the subject
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
            return redirect('blog-home')  # Redirect to home page after successful login
        else:
            return HttpResponse('Invalid login credentials')  # Display error message
    else:
        return render(request, 'blog/login.html')
