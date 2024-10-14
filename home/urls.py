from django.urls import path, include
from .views import HomePage, Months

urlpatterns = [
    path('', HomePage.NoticiasFaker),
    path('sugestions/', HomePage.Sugestions, name='september'),
    path('september/', Months.September),
]   
