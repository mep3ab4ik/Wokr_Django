# Generated by Django 4.0.4 on 2022-05-19 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_menuitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_label',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='links', to='menu_app.menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
