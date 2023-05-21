from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    class Meta:
        model = User
        fields=[
            'username',
            'password1',
            'password2',
            'email'
        ]
    
    