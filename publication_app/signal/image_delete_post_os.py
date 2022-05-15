import os
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from publication_app.models import Post, ImagePost


@receiver(pre_delete, sender=Post)
def pre_delete_post(instance, **kwargs):
    if not instance.pk:
        return False
    get_image = ImagePost.objects.filter(post=instance.pk)
    for image in get_image:
        if image.image:
            os.remove(image.image.path)