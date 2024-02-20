# smartscore/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationFormWithTeacher
from .models import Profile
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = RegistrationFormWithTeacher(request.POST)
        if form.is_valid():
            user = form.save()

            # Check if the user registered as a teacher
            if form.cleaned_data.get('is_teacher'):
                auth_login(request, user)  # Automatically log in the teacher
                return redirect('home')  # Redirect to the home page after successful registration and login

            # For students or other cases, you can add specific logic here
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationFormWithTeacher()

    return render(request, 'register.html', {'form': form})

def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def view_exams(request):
    # Your view logic for viewing exams
    return render(request, 'exams.html')


def home(request):
    # Add any logic you need for the home page
    return render(request, 'home/home.html')  # Make sure you have a corresponding home.html template

def process(request):
    # Add any specific processing for the "Process Exams" page
    return render(request, 'process/process.html')

def exams(request):
    # Add any specific processing for the "Process Exams" page
    return render(request, 'exams/exams.html')

def search_exams(request):
    # Your view logic here
    return render(request, 'search_exams.html')  # Adjust the template name as needed

def classes(request):
    # Your view logic here
    return render(request, 'classes/classes.html')

def students(request):
    # Your view logic here
    return render(request, 'students/students.html')

def about_us(request):
    # Your about_us logic here
    return render(request, 'about_us.html')

def contact(request):
    # Your contact logic here
    return render(request, 'contact.html')

def download_test_paper(request):
    # Assuming 'images/test_paper.png' is the path to your static test paper file
    static_test_paper_path = 'images/test_paper.png'
    return redirect(f'{settings.STATIC_URL}{static_test_paper_path}')

def scan(request):
    # Your logic for the scan page goes here
    return render(request, 'scan.html')