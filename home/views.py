from django.shortcuts import render
from .models import FakeNews
from datetime import datetime
from faker import Faker

class HomePage:
    
    @staticmethod
    def NoticiasFaker(requests):
        
        name = set()
        fake = Faker('pt-BR')
        
        title = fake.catch_phrase()
        
       
        if title in name:
            title = fake.catch_phrase()
        else:
            title = fake.catch_phrase()
            author = fake.name()
            dat = datetime.today().date()
            content = fake.paragraph(nb_sentences=5)
            local = fake.administrative_unit()
            
            
        noticia = FakeNews.objects.create(
            title = title,
            author = author,
            dat = dat,
            content = content,
            local = local
        )
                 
        return render(
                requests, 
                'home/index.html', 
                {'noticia': noticia} # Context
        )
            
    @staticmethod
    def Sugestions(requests):
        return render(
            requests,
            'home/sugestions.html'
    )
    
class Months:
    @staticmethod
    def September(requests):
        
        return render(
            requests,
            'home/september.html'
        )
    
