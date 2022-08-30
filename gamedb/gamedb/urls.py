from django.contrib import admin
from django.urls import path, include
from gamedata import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'videogames', views.VideoGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
