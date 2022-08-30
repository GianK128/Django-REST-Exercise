from django.db import models
from datetime import datetime

# Create your models here.
class Genre(models.Model):
    """
        Modelo que representa un género para uno o más videojuegos
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(180)
    created_at = models.DateTimeField(default=datetime.utcnow())
    updated_at = models.DateTimeField(default=datetime.utcnow())
    
    class Meta:
        db_table = 'genres'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='name_idx')
        ]

class Publisher(models.Model):
    """
        Modelo que representa un publisher para uno o más videojuegos
    """
    trade_name = models.CharField(max_length=60, unique=True)
    founded = models.DateField()
    created_at = models.DateTimeField(default=datetime.utcnow())
    updated_at = models.DateTimeField(default=datetime.utcnow())

    class Meta:
        db_table = 'publishers'
        ordering = ['trade_name']
        indexes = [
            models.Index(fields=['trade_name'], name='trade_name_idx')
        ]

class Platform(models.Model):
    """
        Modelo que representa una plataforma donde pueden estar publicados
        uno o mas juegos
    """
    name = models.CharField(max_length=30, unique=True)
    manufacturer = models.CharField(60)
    created_at = models.DateTimeField(default=datetime.utcnow())
    updated_at = models.DateTimeField(default=datetime.utcnow())

    class Meta:
        db_table = 'platforms'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='name_idx')
        ]

class VideoGame(models.Model):
    """
        Clase que representa un videojuego, puede tener varios generos o plataformas
        en las que está publicado, y un solo publisher
    """
    name = models.CharField(max_length=60)
    published_year = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='games', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, related_name='games', null=True, blank=True)
    platform = models.ManyToManyField(Platform, related_name='games', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow())
    updated_at = models.DateTimeField(default=datetime.utcnow())

    class Meta:
        db_table = 'videogames'
        ordering = ['name']
        indexes = [
            models.Index(fields=['published_year'], name='pub_year_idx'),
            models.Index(fields=['name'], name='name_idx')
        ]
