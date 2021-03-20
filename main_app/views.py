from main_app.forms import ProfileForm, SignupForm, EditForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Article, Comment, Post
from django.contrib.auth import get_user_model
from .forms import PostForm, CommentForm
import datetime
from datetime import date

# Create your views here.

def home(request):
  review = Article.objects.all()
  return render(request, 'home.html', {'review': review})

def about(request):
  return render(request, 'about.html')


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
  comment = Comment.objects.filter(user_id=request.user.id)
  comment_form=CommentForm(request.POST or None)
  comment_amount=len(comment)
  user_info = Profile.objects.get(user_id=request.user.id)
  user_form = EditForm(request.POST or None, instance=user)
  profile_form=ProfileForm(request.POST or None, instance=profile)
  if Post.objects.filter(user_id=request.user.id).order_by('-id'):
    post = Post.objects.filter(user_id=request.user.id).order_by('-id')[0]
  else:
    post = None
  print(post)
  form=PostForm(request.POST or None, instance=profile)
  context = {
    'user':user, 
    'user_info':user_info, 
    'user_form':user_form,
    'profile_form':profile_form,
    'comment_form':comment_form,
    'comment': comment,
    'comment_amount': comment_amount,
    'form': form,
    'post': post
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
    return render(request, 'profile/profileCreation.html', { 'profile_form': profile_form, })

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

# Ask about multiple reviews for the same product, if so change the prety url to ugly url
def review(request, review_product):
  review = Article.objects.get(url=review_product)
  comment = Comment.objects.filter(article_id = review.id)
  number_of_comments = len(comment)
  add_comment_form = CommentForm(request.POST or None)
  return render(request, 'article/review-expanded.html', {'review': review, 'comment': comment, 'add_comment_form': add_comment_form,'number_of_comments':number_of_comments})


def profile_public(request, username):
  user = User.objects.get(username=username)
  user_info = Profile.objects.get(user_id=user.id)
  comment = Comment.objects.filter(user_id=user.id)
  comment_amount=len(comment)
  if Post.objects.filter(user_id=user.id).order_by('-id'):
    post = Post.objects.filter(user_id=user.id).order_by('-id')[0]
  else:
    post = None
  
  context = {
    'user':user, 
    'user_info':user_info, 
    'comment': comment,
    'comment_amount': comment_amount,
    'post':post,
  }
  return render(request, 'profile/public.html', context)

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

@login_required
def add_comment(request, article_id):
  article = Article.objects.get(id = article_id)
  article_product = article.url
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit = False)
    new_comment.user_id = request.user.id
    new_comment.article_id = article_id
    new_comment.creation_date = date.today()
    new_comment.save()
    
  return redirect('review', article_product)

@login_required
def delete_comment(request,comment_id):
  Comment.objects.get(id=comment_id).delete()
  return redirect('profile')

@login_required
def edit_comment(request, comment_id):
  comment = Comment.objects.get(id=comment_id)
  form=CommentForm(request.POST or None, instance=comment)
  if request.POST and form.is_valid():
    form.save()
    return redirect('profile')
  else:
    return redirect ('profile')

