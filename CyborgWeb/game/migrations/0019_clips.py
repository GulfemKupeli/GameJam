# Generated by Django 5.0.3 on 2024-03-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_newsgame_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip_image', models.ImageField(upload_to='clips')),
                ('clip_title', models.CharField(max_length=150)),
            ],
        ),
    ]