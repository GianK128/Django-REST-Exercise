from gamedata.models import Genre, Publisher, Platform, VideoGame
from gamedata.serializers import GenreSerializer, PublisherSerializer, PlatformSerializer, VideoGameSerializer
from rest_framework import viewsets, permissions

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticated]