from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('news/', views.news, name='news'),
    # path('indie/', views.indie, name='indie'),
    path('profile/', views.profile, name='profile'),
    path('comment/', views.comment, name='comment'),
]