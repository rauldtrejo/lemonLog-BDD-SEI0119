from main_app.forms import ProfileForm, SignupForm, EditForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Article, Comment
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
  review = Article.objects.all()
  return render(request, 'home.html', {'review': review})



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = SignupForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('profile_creation')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required  
def profile(request):
  
  user = User.objects.get(id=request.user.id)
  profile = Profile.objects.get(user_id=request.user.id)
  
  user_info = Profile.objects.get(user_id=request.user.id)
  user_form = EditForm(request.POST or None, instance=user)
  profile_form=ProfileForm(request.POST or None, instance=profile)
  context = {
    'user':user, 
    'user_info':user_info, 
    'user_form':user_form,
    'profile_form':profile_form,
  }
  return render(request, 'profile/profile.html', context)

@login_required
def profile_creation(request):
  # create new instance of cat form filled with submitted values or nothing
  profile_form = ProfileForm(request.POST or None)
  # if the form was posted and valid
  if request.POST and profile_form.is_valid():
    # save new instance of a cat
    new_profile = profile_form.save(commit=False)
    new_profile.user = request.user
    new_profile.save()
    # redirect to index
    return redirect('profile')
  else:
    # render the page with the new cat form
    return render(request, 'profile/profileCreation.html', { 'profile_form': profile_form })

@login_required
def profile_edit(request):
  # get a reference to a cat
  user = User.objects.get(id=request.user.id)
  profile = Profile.objects.get(user_id=request.user.id)
  # build a form for the cat filling it with values from the instance or values from the POST request
  user_form = EditForm(request.POST or None, instance=user)
  profile_form=ProfileForm(request.POST or None, instance=profile)
  if request.POST and user_form.is_valid() and profile_form.is_valid():
    # save changes to the cat
    user_form.save()
    profile_form.save()
    # redirect to the detail page
    return redirect('profile')
  else:
    return redirect('profile')

def review(request, review_id):
  review = Article.objects.get(id=review_id)
  return render(request, 'article/review-expanded.html', {'review': review})
