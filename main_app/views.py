from main_app.forms import ProfileForm, SignupForm, EditForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Article, Comment, Post
from .forms import PostForm, CommentForm
from datetime import date

# Create your views here.

# This view takes the user to the homepage
def home(request):
  review = Article.objects.all()
  return render(request, 'home.html', {'review': review})

# This view takes the user to the about page
def about(request):
  return render(request, 'about.html')

# This view will take the user to the signup page and also create a user in the database from the data inputed into the signup page.
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
      error_message = 'Invalid sign up - Username can only be one word, no spaces. Only one account per email and username. Read password requisites.'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# This view is for the user profile. Only a logged in user can access it and it will only show their information.
# This view also passes editing forms for the user information and a picture upload form for their picture profile
# The user also has access to all the comments they've made, and CRUD functionality for their comments.
# A logged in user is only able to edit their own profile and comments, and are unable to edit any other users data.
# There is also logic that will recognize if the user has a profile picture uploaded or not, and will either display
# the picture they uploaded or a placeholder image.
@login_required  
def profile(request):
  user = User.objects.get(id=request.user.id)
  profile = Profile.objects.get(user_id=request.user.id)
  comment = Comment.objects.filter(user_id=request.user.id)
  comment_form=CommentForm(request.POST or None)
  comment_amount=len(comment)
  user_form = EditForm(request.POST or None, instance=user)
  profile_form=ProfileForm(request.POST or None, instance=profile)
  if Post.objects.filter(user_id=request.user.id).order_by('-id'):
    user_photo = Post.objects.filter(user_id=request.user.id).order_by('-id')[0]
  else:
    user_photo = None
  photo_upload_form=PostForm(request.POST or None, instance=profile)
  context = {
    'user':user, 
    'profile':profile, 
    'user_form':user_form,
    'profile_form':profile_form,
    'comment_form':comment_form,
    'comment': comment,
    'comment_amount': comment_amount,
    'photo_upload_form': photo_upload_form,
    'user_photo': user_photo
  }
  return render(request, 'profile/profile.html', context)

# After creating an account, the user is redirected to the profile creation page
# They need to input additional information to complete their profile.
# The profile model takes a user's age and location.
@login_required
def profile_creation(request):
  profile_form = ProfileForm(request.POST or None)
  if request.POST and profile_form.is_valid():
    new_profile = profile_form.save(commit=False)
    new_profile.user = request.user
    new_profile.save()
    return redirect('profile')
  else:
    return render(request, 'profile/profileCreation.html', { 'profile_form': profile_form, })

# This view executes the update function for the users information when they make anychanges via the profile page.
@login_required
def profile_edit(request):
  user = User.objects.get(id=request.user.id)
  profile = Profile.objects.get(user_id=request.user.id)
  user_form = EditForm(request.POST or None, instance=user)
  profile_form=ProfileForm(request.POST or None, instance=profile)
  if request.POST and user_form.is_valid() and profile_form.is_valid():
    user_form.save()
    profile_form.save()
    return redirect('profile')
  else:
    return redirect('profile')


# This view renders the review article page, and passes on all the necessary information that will be displayed on the page.
def review(request, review_product):
  review = Article.objects.get(url=review_product)
  comment = Comment.objects.filter(article_id = review.id)
  number_of_comments = len(comment)
  add_comment_form = CommentForm(request.POST or None)
  context= {
    'review': review, 
    'comment': comment, 
    'add_comment_form': add_comment_form,
    'number_of_comments':number_of_comments,
  }
  return render(request, 'article/review-expanded.html', context)


# This view renders a public version of a users profile, where anybody can see the previous comments that a user has made
# The users who visit this public profile cannot edit any data of other users.
def profile_public(request, username):
  user = User.objects.get(username=username)
  profile = Profile.objects.get(user_id=user.id)
  comment = Comment.objects.filter(user_id=user.id)
  comment_amount=len(comment)
  if Post.objects.filter(user_id=user.id).order_by('-id'):
    post = Post.objects.filter(user_id=user.id).order_by('-id')[0]
  else:
    post = None
  context = {
    'user':user, 
    'profile':profile, 
    'comment': comment,
    'comment_amount': comment_amount,
    'post':post,
  }
  return render(request, 'profile/public.html', context)

# This view allows a user to upload a new picture and replace their existing one.
@login_required
def photo_edit(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False) 
        post.user_id = request.user.id
        post.save()
  else:
    form = PostForm()
  try:
    post = Post.objects.all()
  except Post.DoesNotExist:
    post = None
  return redirect('profile')

# This view executes the post comment function.
@login_required
def add_comment(request, article_id):
  review = Article.objects.get(id = article_id)
  review_url = review.url
  comment_form = CommentForm(request.POST)
  # The following line of code associates the user image to the comment, which will then be used
  # to display the user's image next to their comment in the comment section
  if Post.objects.filter(user_id=request.user.id).order_by('-id'):
    user_photo = Post.objects.filter(user_id=request.user.id).order_by('-id')[0]
  # The following line is hardcoded to a default placeholder image in the database
  else:
    user_photo = Post.objects.get(id=15)
  if comment_form.is_valid():
    new_comment = comment_form.save(commit = False)
    new_comment.user_id = request.user.id
    new_comment.post_id = user_photo.id
    new_comment.article_id = article_id
    new_comment.creation_date = date.today()
    new_comment.save()

  return redirect('review', review_url)

@login_required
def delete_comment(request,comment_id):
  Comment.objects.get(id=comment_id).delete()
  return redirect('profile')

@login_required
def edit_comment(request, comment_id):
  comment = Comment.objects.get(id=comment_id)
  comment_form = CommentForm(request.POST or None, instance=comment)
  if request.POST and form.is_valid():
    comment_form.save()
    return redirect('profile')
  else:
    return redirect ('profile')

