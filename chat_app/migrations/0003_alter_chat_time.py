# Generated by Django 4.0.5 on 2022-06-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_chat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]