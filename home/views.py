from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class HomePage:
    ...
    
def ret(requests):
    return render(
        requests, 
        'home/index.html'
    )
    