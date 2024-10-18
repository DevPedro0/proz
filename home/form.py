from django import forms
from .models import Formulario

class Form(forms.Form):
    class Meta:
        model = Formulario
        


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['firstname', 'lastname', 'e_mail', 'notes', 'cidade', 'job']
