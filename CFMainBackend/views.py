from django.shortcuts import render
from .serializers import ActorSerializer, ActorVideoSerializer, ActorPhotoSerializer
from rest_framework import viewsets
from .models import Actor, ActorVideo, ActorPhoto
# Create your views here.

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_fields = ('name', 'email')


class ActorVideosViewSet(viewsets.ModelViewSet):
    queryset = ActorVideo.objects.all()
    serializer_class = ActorVideoSerializer


class ActorPhotosViewSet(viewsets.ModelViewSet):
    queryset = ActorPhoto.objects.all()
    serializer_class = ActorPhotoSerializer