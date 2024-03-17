# Generated by Django 5.0.3 on 2024-03-15 10:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_images_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='current_status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], default='Downloaded', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='game',
            name='hours_played',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
