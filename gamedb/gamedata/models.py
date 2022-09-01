from django.db import models

# Create your models here.
class Genre(models.Model):
    """
        Modelo que representa un género para uno o más videojuegos
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
    class Meta:
        db_table = 'genres'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='genre_name_idx')
        ]

class Publisher(models.Model):
    """
        Modelo que representa un publisher para uno o más videojuegos
    """
    trade_name = models.CharField(max_length=60, unique=True)
    founded = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.trade_name}"

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
    manufacturer = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'platforms'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='platform_name_idx')
        ]

class VideoGame(models.Model):
    """
        Clase que representa un videojuego, puede tener varios generos o plataformas
        en las que está publicado, y un solo publisher
    """
    name = models.CharField(max_length=60)
    published_year = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='games', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games', null=True, blank=True)
    platform = models.ManyToManyField(Platform, related_name='games', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
    class Meta:
        db_table = 'videogames'
        ordering = ['name']
        indexes = [
            models.Index(fields=['published_year'], name='pub_year_idx'),
            models.Index(fields=['name'], name='videogame_name_idx')
        ]
