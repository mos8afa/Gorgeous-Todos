from django.forms import ModelForm
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone']

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        