# Generated by Django 4.0.4 on 2022-05-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagine',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y'),
        ),
    ]
