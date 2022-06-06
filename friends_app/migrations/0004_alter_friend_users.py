# Generated by Django 4.0.4 on 2022-06-03 15:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends_app', '0003_friend_remove_friendrequest_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(related_name='test_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
