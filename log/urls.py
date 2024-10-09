from django.urls import path
from .views import Log, Register

urlpatterns = [
    path('login/', Log),
    path('register/', Register)
]
