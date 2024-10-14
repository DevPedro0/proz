from django.urls import path
from .views import Podcasts

urlpatterns = [
    path('podcast/', Podcasts.PodCast, name = 'podcast')
]
    