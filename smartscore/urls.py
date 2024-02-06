from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.register, name='register'), 
    path('process/', views.process, name='process'),
    path('search-exams/', views.search_exams, name='search_exams'),
    path('exams/', views.exams, name='exams'),
    path('login/', views.user_login, name='login'),
    path('classes/', views.classes, name='classes'),
    path('about_us/', views.about_us, name='about_us'),
    path('students/', views.students, name='students'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Use LogoutView here
    # Add more URL patterns as needed
]
