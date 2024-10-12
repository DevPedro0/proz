from django.urls import path, include
from .views import TestFaker


urlpatterns = [
    path('', TestFaker.NoticiasFaker),
    
]
