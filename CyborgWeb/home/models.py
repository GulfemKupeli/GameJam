from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from game.models import Game


class UserProfile(models.Model):
    games_downloaded = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    screenshots = models.IntegerField(default=0)
    clips = models.IntegerField(default=0)
    friends_online = models.IntegerField(default=False)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/', default="images/default")

    def __str__(self):
        return self.user.username


class Setting(models.Model):
    STATUS = (('True', 'True'), ('False', 'False'),)
    title = models.CharField(max_length=150)
    icon = models.ImageField(blank=True, upload_to='images/')
    logo = models.ImageField(blank=True, upload_to='images/')
    banner_image = models.ImageField(upload_to='banners/', default='banners/default_banner.jpg')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'Comment by {self.name} at {self.created_at}'
