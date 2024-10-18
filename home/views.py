from django.shortcuts import render, redirect
from .models import ProzNews, Locals
from datetime import datetime
from .form import FormularioForm

class HomePage:
    
    @staticmethod
    def NoticiasFaker(requests):
        
        return render(
                requests, 
                'home/index.html', 
        )
    
class Months:
    @staticmethod
    def September(requests):        
        return render(
            requests,
            'home/september.html',
          
        )

class Contact:
    
    @staticmethod
    def contact(request):
        if request.method == 'POST':
            form = FormularioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/app/enquetes/')  # Redireciona para a página correta
        else:
            form = FormularioForm()

        return render(
            request,  
            'home/contact.html',  # Template correto
            {'localfinal': form}
        )
