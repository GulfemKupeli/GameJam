# Generated by Django 5.0.3 on 2024-03-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_featuredgame_images_featured_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='current_status',
        ),
        migrations.RemoveField(
            model_name='game',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='hours_played',
        ),
        migrations.AddField(
            model_name='game',
            name='downloads',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]