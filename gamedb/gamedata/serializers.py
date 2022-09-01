from rest_framework import serializers
from gamedata.models import Genre, Publisher, Platform, VideoGame

# Modelo de género
class GenreSerializer(serializers.ModelSerializer):    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        model = Genre
        fields = ['name', 'description', 'created_at', 'updated_at', 'games']

# Modelo de publisher
class PublisherSerializer(serializers.ModelSerializer):
    def __str__(self) -> str:
        return f"{self.trade_name}"
    
    class Meta:
        model = Publisher
        fields = ['trade_name', 'founded', 'created_at', 'updated_at', 'games']

# Modelo de plataforma
class PlatformSerializer(serializers.ModelSerializer):
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        model = Platform
        fields = ['name', 'manufacturer', 'created_at', 'updated_at', 'games']

# Modelo de videojuego
class VideoGameSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Genre.objects.all()
    )
    publisher = PublisherSerializer()
    # publisher_id = serializers.PrimaryKeyRelatedField(
    #     write_only=True,
    #     source='publisher',
    #     queryset=Publisher.objects.all()
    # )
    platform = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Platform.objects.all()
    )
    
    def to_internal_value(self, data):
        self.fields['publisher'] = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
        return super().to_internal_value(data)

    def to_representation(self, validated_data):
        response = super().to_representation(validated_data)
        response['publisher'] = PublisherSerializer(validated_data.publisher).data
        return response

    class Meta:
        model = VideoGame
        fields = ['name', 'published_year', 'genres', 'publisher', 'publisher_id', 'platform', 'created_at', 'updated_at']
