import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from publication_app.models import Post, HashtagPost
from tag_app.models import Hashtag


@receiver(post_save, sender=Post)
def post_save_hashtag(sender, instance, **kwargs):
    if not instance.pk:
        return False
    post = sender.objects.get(pk=instance.pk)
    hashtags = re.findall(r'#[A-zА-яёЁ]+', instance.text)
    if hashtags:
        for hashtag in hashtags:
            tag = Hashtag.objects.filter(hashtag=hashtag)
            if tag:
                tag = Hashtag.objects.get(hashtag=hashtag)
                HashtagPost.objects.create(hashtag=tag, post=post)
            else:
                tag_obj = Hashtag(hashtag=hashtag.lower())
                tag_obj.save()
                HashtagPost.objects.create(hashtag=tag_obj, post=post)

