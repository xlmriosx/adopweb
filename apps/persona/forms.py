from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.persona.models import Persona
from datetime import date

class RegistroFormulario(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
        	'last_name', 
	        'email', 
    	
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre', 
        	'last_name': 'Apellido', 
	        'email': 'Email',        	
        }


class PersonaFormulario(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre', 
        	'apellido', 
	        'email', 
            #'imagen',
            'fechaNac',
            'telcel',
            'numero',
            'denuncias',  	
        ]
        labels = {
            'nombre': 'Nombre', 
        	'apellido': 'Apellido', 
	        'email': 'Email', 
            #'imagen': 'Imagen',
            'fechaNac': 'Fecha Nacimiento',
            'telcel': 'Telefono/Celular',
            'numero': 'Numero',
            'denuncias': 'Denuncias',        	
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}), 
        	'apellido': forms.TextInput(attrs={'class':'form-control'}), 
	        'email': forms.TextInput(attrs={'class':'form-control'}), 
            #'imagen',
            'fechaNac': forms.SelectDateWidget(empty_label=("Año", "Mes", "Día"), attrs={'class':'form-control'}),
            'telcel': forms.Select(attrs={'class':'form-control'}),
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'denuncias': forms.TextInput(attrs={'class':'form-control'}), 
			'adoptante': forms.Select(attrs={'class':'form-control'}),
        	'animal': forms.Select(attrs={'class':'form-control'}), 
	        'solicitud': forms.TextInput(attrs={'class':'form-control'}),        	
        }

