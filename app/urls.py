from django.urls import path
from .views import Podcasts, Canais, Enquetes
urlpatterns = [
    path('podcast/', Podcasts.PodCast, name = 'podcast'),
    path('canais/', Canais, name = 'canais'),
    path('enquetes/',Enquetes, name='enquetes' )
]
    