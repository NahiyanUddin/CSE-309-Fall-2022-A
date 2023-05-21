from django.shortcuts import render
from course.forms import CourseForm
from course.models import Course

# Create your views here.

def course_view(request):
    
    
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
        
    course_form = CourseForm()
    
    context = {
        'course_form':course_form
    }
    return render(request,'course/course.html', context)

def coursev2_view(request):
    
    if request.method == 'POST':
        code = request.POST['code']        
        title = request.POST['title']        
        description = request.POST['description']
        
        course_object = Course(code=code, title=title, description=description)
        course_object.save()
                
        
    return render(request,'course/course_v2.html')

def coursev3_view(request):
    
    if request.method == 'POST':
        course_form = CourseForm(request.POST)   
        
        if course_form.is_valid() :
            course_form.save()     
        
    return render(request,'course/course_v2.html')


def coursev4_view(request, code):
    context = {
        'code':code
    }
    return render(request, 'course/course_v4.html',context)
