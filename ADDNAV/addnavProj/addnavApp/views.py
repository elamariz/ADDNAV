import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required

# Initialize the logger
logger = logging.getLogger(__name__)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get the backend path
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)
            logger.debug(f"New user signed up: {user.username}")
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Get the backend path
                backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user, backend=backend)
                logger.debug(f"User logged in: {user.username}")
                return redirect('homepage')
            else:
                logger.warning(f"Failed login attempt for username: {username}")
                form.add_error(None, "Invalid username or password")
    return render(request, 'login.html', {'form': form})

@login_required
def homepage_view(request):
    return render(request, 'homepage.html')

@login_required
def medroville_view(request):
    return render(request, 'medroville.html')

@login_required
def relos_view(request):
    return render(request, 'relos.html')

@login_required
def aquebo_view(request):
    return render(request, 'aquebo.html')

@login_required
def felicitas_view(request):
    return render(request, 'felicitas.html')

@login_required
def dorm_view(request):
    return render(request, 'dorm.html')

@login_required
def about_view(request):
    return render(request, 'about.html')

@login_required
def contact_view(request):
    return render(request, 'contact.html')

@login_required
def faq_view(request):
    return render(request, 'addnavApp/faq.html')

@login_required
def logout_view(request):
    logger.debug(f"User logged out: {request.user.username}")
    logout(request)
    return redirect('login')
