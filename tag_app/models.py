from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=128, null=False, blank=False)


    def __str__(self):
        return f'{self.tag}'


