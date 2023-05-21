from django.shortcuts import render, redirect
from course.models import *
from userprofile.models import *
from django.contrib.auth.forms import UserCreationForm
from home.forms import UserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    # form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            # auto login
            username = request.POST['username']
            password = request.POST['password1']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
            else:
                print('User not found')
            
            return redirect('home')
        else:
            context = {
                'form':form
                }
            return render(request, 'signup.html', context)
    form = UserSignupForm()
    context = {
            'form':form
        }
    return render(request, 'signup.html', context)


def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # we have to login
            login(request, user)
            
            return redirect('home')
        else:
            error = 'Username and password not matched!'
            context = {
                'error' : error
            }
            return render(request, 'login.html', context)
        
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def password_change_view(request):
    error = ""
    
    if request.method=='POST':
        username = request.user.username
        current_password = request.POST['password']
        
        user = authenticate(username=username, password = current_password)
        
        if user is not None:
            
            current_user = User.objects.get(username=username)
            
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            
            if password1 == password2:
                current_user.set_password(password1)
                current_user.save() 
            else:
                error = "New Password and Confirm Password do not match."
        else:
            error = "Current Password does not match."
            
    context ={
        'error' : error
    }  
    
    return render(request, 'password_change.html', context)


@login_required
def test_view(request):
    print("Hello")
    
    query_result = Course.objects.get(code='CSE 305')
    
    course = query_result[0]
    course.delete()   
    
    userprofile = UserProfile(phone_no='015000000', user = User.objects.get(id=1))
    
    return render(request, 'home.html')
