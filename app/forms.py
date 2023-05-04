from django import forms
from app.models import *


class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        Password=forms.PasswordInput()
        widgets={'password':Password }
class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['Address','Profile_pic']