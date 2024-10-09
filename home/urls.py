from django.urls import path, include
from .views import ret


urlpatterns = [
    path('', ret ),
    
]
