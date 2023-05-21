from django.contrib.auth.forms import forms 
from course.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields = [
            'code',
            'title',
            'description'
        ]