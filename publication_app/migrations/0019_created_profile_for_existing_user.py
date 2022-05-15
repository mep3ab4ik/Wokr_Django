from django.db import migrations


def created_profile_for_existing_user(apps, schemas_editors):
    user_model = apps.get_model('auth', 'User')
    profile_model = apps.get_model('publication_app', 'Profile')

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0018_alter_imagepost_image'),
    ]

    operations = [
        migrations.RunPython(created_profile_for_existing_user),
    ]
