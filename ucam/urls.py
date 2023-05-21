"""ucam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from home.views import *
from course.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',home_view, name='home'),
    
    path('signup/',signup_view, name='signup'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('password-change/',password_change_view, name='password_change'),
    
    
    path('test/',test_view, name='test'),
    path('course/',course_view, name='course'),
    path('coursev2/',coursev2_view, name='course2'),
    path('coursev3/',coursev3_view, name='course3'),
    path('coursev4/<int:code>',coursev4_view, name='course4'),
]
