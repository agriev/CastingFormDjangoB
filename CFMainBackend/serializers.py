from CFMainBackend.models import Actor
from rest_framework import serializers


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'email', 'headshot')


