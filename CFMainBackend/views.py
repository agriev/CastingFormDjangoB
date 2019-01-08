from django.shortcuts import render
from .serializers import ActorSerializer
from rest_framework import viewsets
from .models import Actor
# Create your views here.

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_fields = ('name', 'email')