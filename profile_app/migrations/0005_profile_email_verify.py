# Generated by Django 4.0.4 on 2022-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
