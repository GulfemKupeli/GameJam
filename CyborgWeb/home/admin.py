from django.contrib import admin

from game.models import Clips
from home.models import UserProfile, Setting, Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Setting)
admin.site.register(Clips)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'created_at']

admin.site.register(Comment, CommentAdmin)