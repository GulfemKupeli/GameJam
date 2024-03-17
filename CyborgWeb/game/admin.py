from django.contrib import admin
from .models import Game, Images, GameTrailer, NewsGame


class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'image_tag']
    readonly_fields = ['image_tag']


class GameImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class ImagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game)
admin.site.register(GameTrailer)
admin.site.register(NewsGame)
