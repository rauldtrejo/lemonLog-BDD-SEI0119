from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('duplicate_email')
        return email    

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)