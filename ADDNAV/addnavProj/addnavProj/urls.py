"""
URL configuration for addnavProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from addnavApp import views

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='redirect_to_login'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('dorm/', views.dorm_view, name='dorm'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('logout/', views.logout_view, name='logout'),
    path('medroville/', views.medroville_view, name='medroville'),
    path('felicitas/', views.felicitas_view, name='felicitas'),
    path('relos/', views.relos_view, name='relos'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('aquebo/', views.aquebo_view, name='aquebo'),
    # Add more paths as needed
]



