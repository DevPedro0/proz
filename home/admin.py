from django.contrib import admin
from .models import Formulario

# Register your models here.

@admin.register(Formulario)
class LogAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'e_mail', 'cidade', 'job')