# Generated by Django 4.0.4 on 2022-05-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag_app', '0002_rename_tags_tag_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='tags',
        ),
    ]