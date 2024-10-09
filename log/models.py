from django.db import models
    
class Register(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=128)
    date_joined = models.DateField()
    
    class Meta:
        ...