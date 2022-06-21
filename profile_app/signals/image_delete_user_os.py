import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from profile_app.models import Profile


@receiver(pre_save, sender=Profile)
def image_delete_user(sender, instance, **kwargs):
    """
    Функция удаления изображение старого изображение.
    Когда пользователь меняет фотографию, то старая фотография удаляется из media
    """
    if not instance.pk:
        return False
    # Проверяем наличие фотографии
    if sender.objects.get(pk=instance.pk).photo:
        # Записываем в переменную старую фотку
        old_img = sender.objects.get(pk=instance.pk).photo
        # Записываем в переменную новую фотку
        new_img = instance.photo
        # Сравниваем фотки
        if old_img != new_img:
            # Если фотография новая, то проверяем путь и затем удаляем
            if os.path.isfile(old_img.path):
                os.remove(old_img.path)
        else:
            return False
