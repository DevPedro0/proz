from django.urls import path
from .views import Podcasts, Canais

urlpatterns = [
    path('podcast/', Podcasts.PodCast, name = 'podcast'),
    path('canais/', Canais, name = 'canais')
]
    