from django.urls import path
from .views import HomePage, Months, Contact

urlpatterns = [
    path('', HomePage.NoticiasFaker),
    path('contact/', Contact.contact, name='contact'),
    path('september/', Months.September),
]   
