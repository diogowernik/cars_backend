# Generated by Django 3.2 on 2021-11-18 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
    ]
