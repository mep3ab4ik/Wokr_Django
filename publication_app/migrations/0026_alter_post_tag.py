# Generated by Django 4.0.4 on 2022-05-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_app', '0004_rename_tags_tag_tag'),
        ('publication_app', '0025_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='tag_app.tag'),
        ),
    ]
