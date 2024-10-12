from django.shortcuts import render

from .models import FakeNews
from datetime import datetime

from faker import Faker

# Create your views here.

class TestFaker:
    
    @staticmethod
    def NoticiasFaker(requests):
        fake = Faker('pt-br')
        
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

