from django.db import models

class FakeNews(models.Model):
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    dat = models.DateField()
    content = models.TextField(unique=True)
    local = models.CharField(max_length=50, default='Desconhecido')
    
    def __str__(self):
        return str(self.title)
