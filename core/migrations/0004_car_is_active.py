# Generated by Django 3.2 on 2021-11-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_user_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
