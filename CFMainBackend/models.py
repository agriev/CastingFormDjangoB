from django.db import models
# from django.conf import settings
from django.utils.html import format_html
from enum import Enum

# Create your models here.
from django.db.models.fields.files import ImageFieldFile

# class SexChoice(Enum):
#     MALE = 'Male'
#     FEMALE = 'Female'


class Actor(models.Model):
    name: str = models.CharField(max_length=200)
    last_name: str = models.CharField(max_length=200)
    gender = models.CharField(verbose_name='Sex', max_length=6, choices=[('m', 'Male'),
                                                                         ('f', 'Female'),
                                                                         ])#[(tag, tag.value) for tag in SexChoice])
    height = models.DecimalField(max_digits=10, decimal_places=2)# santimeters
    based = models.CharField(max_length=200)  # Please, specify city and country where you are currently based TODO: One to Many
    citizenship = models.CharField(max_length=400)  # Please, specify all your citizenships, country where you hold your passport from (can be more than one) TODO: Many to many
    date_of_birth = models.DateField(verbose_name='Date of birth')
    mobile = models.CharField(max_length=25)  # TODO: add validators
    email = models.EmailField()
    known_for = models.TextField()  # TODO 3 fields not one
    main_headshot: ImageFieldFile = models.ImageField(null=True, blank=True, upload_to='images')
    cv = models.FileField(null=True, blank=True, upload_to='cvs')
    imdb_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)

    def __str__(self):
        return self.last_name + " " + self.last_name


class ActorPhoto(models.Model):
    file = models.ImageField(upload_to='images')
    description = models.TextField()
    actor = models.ForeignKey(to=Actor, on_delete=models.CASCADE, related_name='photos')


class ActorVideo(models.Model): # TODO: Video maybe different to Showreel. what's the difference - we never know
    file = models.FileField(upload_to='videos')
    description = models.TextField()
    actor = models.ForeignKey(to=Actor, on_delete=models.CASCADE, related_name='videos')
