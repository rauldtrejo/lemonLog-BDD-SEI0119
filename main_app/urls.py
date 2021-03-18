from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/signup/', views.signup, name="signup"),
    path('profile/', views.profile, name='profile'),
    path('profile/creation/', views.profile_creation, name='profile_creation'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('user/<str:username>/', views.profile_public, name="profile_public"),
    path('reviews/<str:review_product>/', views.review, name='review'),
    path('test/', views.test, name='test')
]
