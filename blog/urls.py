from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('', views.user_login, name='user-login'),  # Add this URL pattern for login
]

