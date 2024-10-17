from django.db import models

class FakeNews(models.Model):
    
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