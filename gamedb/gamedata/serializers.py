from rest_framework import serializers
from gamedata.models import Genre, Publisher, Platform, VideoGame

# Modelo de género
class GenreSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Genre
        fields = ['name', 'description', 'created_at', 'updated_at', 'games']

# Modelo de publisher
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['trade_name', 'founded', 'created_at', 'updated_at', 'games']

# Modelo de plataforma
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['name', 'manufacturer', 'created_at', 'updated_at', 'games']

# Modelo de videojuego
class VideoGameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    publisher = PublisherSerializer()
    platform = PlatformSerializer(many=True)
    
    class Meta:
        model = VideoGame
        fields = ['name', 'published_year', 'genres', 'publisher', 'platform', 'created_at', 'updated_at']
