from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/creation/', views.profile_creation, name='profile_creation'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('user/<str:username>/', views.profile_public, name='profile_public'),
    path('reviews/<str:review_product>/', views.review, name='review'),
    # path('test/', views.test, name='test'),
    path('profile/photo_edit/', views.photo_edit, name='photo_edit'),
    path('reviews/add_comment/<int:article_id>/', views.add_comment, name='add_comment')
]
