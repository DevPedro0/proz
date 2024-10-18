from django.db import models

class ProzNews(models.Model):
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    dat = models.DateField()
    content = models.TextField(unique=True)
    local = models.CharField(max_length=50, default='Desconhecido')
    
    def __str__(self):
        return str(self.title)


class Sugestions(models.Model):
    
    THEMES_CHOICES  = [
        ("A", "Arnold"),
        ('B', "Beraldo")
    ]    
    
    sugestions = models.TextField()
    name = models.CharField(max_length=50)
    themes_default = models.CharField(
        max_length=30,
        unique= True,
        choices= THEMES_CHOICES
    )
    

class Locals(models.Model):
    local = models.CharField(max_length=50)
    
  # models.py
from django.db import models

# models.py
from django.db import models

class Formulario(models.Model):
    ESTADOS_BRASIL = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=150)
    notes = models.TextField()
    cidade = models.CharField(max_length=2, choices=ESTADOS_BRASIL)
    job = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
