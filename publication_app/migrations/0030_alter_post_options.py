# Generated by Django 4.0.4 on 2022-05-20 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0029_alter_imagepost_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time', '-id'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]