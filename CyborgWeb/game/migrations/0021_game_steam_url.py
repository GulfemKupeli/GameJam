# Generated by Django 5.0.3 on 2024-03-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_clips_clip_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='steam_url',
            field=models.URLField(blank=True),
        ),
    ]
