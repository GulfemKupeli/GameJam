from random import sample
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from game.models import GameTrailer, NewsGame, Clips
from .forms import CommentForm
from .models import Game, Setting, UserProfile


def home(request):
    games = Game.objects.all()
    setting = Setting.objects.first()
    most_popular = Game.objects.all()[:12]
    gaming_library = Game.objects.all()[:5]
    context = {'setting': setting, 'games': games, 'most_popular': most_popular, 'gaming_library': gaming_library}
    return render(request, 'homebase.html', context)


def discover(request):
    featured_games = Game.objects.filter(featured=True)
    trailer_games = GameTrailer.objects.all()
    top_downloaded_games = Game.objects.filter(featured=False).order_by('-downloads')[:3]
    setting = Setting.objects.first()
    context = {'setting': setting, 'featured_games': featured_games, 'top_downloaded_games': top_downloaded_games,
               'trailer_games': trailer_games}
    return render(request, 'discover.html', context)


def news(request):
    games = Game.objects.all()[:6]
    all_games = Game.objects.all()
    random_games = sample(list(all_games), min(len(all_games), 6))
    setting = Setting.objects.first()
    news_game = NewsGame.objects.all()
    context = {'setting': setting, 'news_game': news_game, 'games': games, 'random_games': random_games}
    return render(request, 'news.html', context)


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    all_games = Game.objects.all()
    random_games = sample(list(all_games), min(len(all_games), 6))
    setting = Setting.objects.first()
    clips = Clips.objects.all()
    context = {'setting': setting, 'user_profile': user_profile, 'clips': clips, 'random_games': random_games}
    return render(request, 'profile.html', context)


def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discover')
    else:
        form = CommentForm()

    return render(request, 'discover.html', {'form': form})
