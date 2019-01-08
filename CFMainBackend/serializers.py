from CFMainBackend.models import Actor, ActorVideo, ActorPhoto
from rest_framework import serializers



class VideoSerializer(serializers.HyperlinkedModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.name')

    class Meta:
        model = ActorVideo
        fields = ('file', 'description', 'actor')

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(many=True,  queryset=ActorVideo.objects.all())#HyperlinkedRelatedField(many=True, view_name='video-detail', read_only=True)
    photos = serializers.PrimaryKeyRelatedField(many=True,  queryset=ActorPhoto.objects.all())#HyperlinkedRelatedField(many=True, view_name='video-detail', read_only=True)

    class Meta:
        model = Actor
        # fields = ('name', 'email', 'headshot')
        # fields = [field.name for field in Actor._meta.get_fields(include_parents=False, include_hidden=False)]
        fields = ['photos', 'videos', 'id', 'name', 'last_name', 'gender', 'height', 'based', 'citizenship', 'date_of_birth',
         'mobile', 'email', 'known_for', 'main_headshot', 'cv', 'imdb_link', 'instagram_link', 'facebook_link']


