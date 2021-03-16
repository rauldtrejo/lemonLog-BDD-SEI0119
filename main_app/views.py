from main_app.forms import ProfileForm, SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
  return render(request, 'home.html')



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
  profile = User.objects.get(id=request.user.id)
  user_info = Profile.objects.get(user_id=request.user.id)
  return render(request, 'profile/profile.html', {'user':profile, 'user_info':user_info})

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


