# Generated by Django 5.0.3 on 2024-03-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_clips'),
    ]

    operations = [
        migrations.AddField(
            model_name='clips',
            name='clip_url',
            field=models.URLField(blank=True),
        ),
    ]
