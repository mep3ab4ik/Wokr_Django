# Generated by Django 4.0.4 on 2022-05-27 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
        ('publication_app', '0037_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_app.media'),
        ),
    ]
