# Generated by Django 5.0.3 on 2024-03-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_userprofile_user_userprofile_clips_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip_image', models.ImageField(upload_to='clips')),
            ],
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Clip',
        ),
        migrations.DeleteModel(
            name='Screenshot',
        ),
    ]
