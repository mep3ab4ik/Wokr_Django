# Generated by Django 4.0.4 on 2022-05-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
