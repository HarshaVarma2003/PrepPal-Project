# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('help/', views.help, name='blog-help'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject-detail'),
    path('forums/', views.forum_list, name='forum-list'),
    path('forums/<int:forum_id>/', views.forum_detail, name='forum-detail'),
    path('forums/new/', views.create_forum, name='create-forum'),
    path('', views.user_login, name='user-login'),
]

