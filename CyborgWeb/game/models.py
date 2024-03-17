from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Game(models.Model):
    STATUS = (
        ('Downloaded', 'Downloaded'),
        ('Not_Downloaded', 'Not_Downloaded'),
    )
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    downloads = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/', default="images/default.jpg")
    featured = models.BooleanField(default=False)
    hours_played = models.PositiveIntegerField(default=20)
    date_added = models.DateField(default=timezone.now)
    current_status = models.CharField(max_length=50, choices=STATUS, default='Downloaded')
    steam_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src= "{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class FeaturedGame(models.Model):
    title = models.CharField(max_length=100)
    downloads = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, upload_to='images/', default="images/default.jpg")

    def __str__(self):
        return self.title


class NewsGame(models.Model):
    header = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/', default="images")
    image2 = models.ImageField(blank=True, upload_to='images/', default="images")
    image3 = models.ImageField(blank=True, upload_to='images/', default="images")
    image4 = models.ImageField(blank=True, upload_to='images/', default="images")
    image5 = models.ImageField(blank=True, upload_to='images/', default="images")
    developer = models.CharField(max_length=50)
    storage = models.CharField(max_length=20)
    trailer_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class GameTrailer(models.Model):
    title = models.CharField(max_length=100)
    trailer_image = models.ImageField(blank=True, upload_to='images/', default="images/default.jpg")
    developer = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Images(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    featured_game = models.ForeignKey(FeaturedGame, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Clips(models.Model):
    clip_image = models.ImageField(upload_to='clips')
    clip_title = models.CharField(max_length=150)
    clip_url = models.URLField(blank=True)

    def __str__(self):
        return self.clip_title
