from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('help/', views.help, name='blog-help'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('', views.user_login, name='user-login'),  # Add this URL pattern for login
]
