# Generated by Django 5.0.3 on 2024-03-13 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_setting_userprofile_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='description',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='email',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpemail',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtppassword',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpport',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpserver',
        ),
    ]
