# Generated by Django 5.0.3 on 2024-03-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_userprofile_user_name_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
