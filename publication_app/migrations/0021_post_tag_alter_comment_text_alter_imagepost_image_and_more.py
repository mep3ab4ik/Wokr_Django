# Generated by Django 4.0.4 on 2022-05-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag_app', '0001_initial'),
        ('publication_app', '0020_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tagpost', to='tag_app.tag'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=256, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, null=True, verbose_name='Доступна всем ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст к посту'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название поста'),
        ),
    ]
