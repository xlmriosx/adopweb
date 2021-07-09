from django import forms
from apps.adopcion.models import Adopcion
from datetime import date


class AdopcionFormulario(forms.ModelForm):

    class Meta:
        model = Adopcion

        fields = [
            'adoptante',
        	'animal', 
	        'solicitud',   	
        ]
        labels = {
            'adoptante': 'Adoptante',
        	'animal': 'Animal', 
	        'solicitud': 'Solicitud',        	
        }
        widgets = {
            'adoptante': forms.Select(attrs={'class':'form-control'}),
        	'animal': forms.Select(attrs={'class':'form-control'}), 
	        'solicitud': forms.TextInput(attrs={'class':'form-control'}),        	
        }

