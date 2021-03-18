from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_age', 'location']

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo',)