from django import forms
from models import User
class signupform(forms.ModelForm):
    class meta:
        model=User
        field=['email','password','name','last_name ']

    class LoginForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email', 'password']