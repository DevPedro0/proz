from django.shortcuts import render

# Create your views here.

def Log(requests):
    return render(
        requests, 
        'log/singin.html'
    )
    
    
def Register(requests):
    return render(
        requests, 
        'log/register.html'
    )