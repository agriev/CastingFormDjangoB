from django.db import models
# from django.conf import settings
from django.utils.html import format_html

# Create your models here.
from django.db.models.fields.files import ImageFieldFile


class Actor(models.Model):
    name: str = models.CharField(max_length=200)
    email = models.EmailField()
    headshot: ImageFieldFile = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.name

class ActorVideo(models.Model):
    file = models.FileField(upload_to='videos')
    description = models.TextField()
    actor = models.ForeignKey(to=Actor, on_delete=models.CASCADE, related_name='videos')
