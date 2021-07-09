from django import forms
from apps.mascota.models import Mascota
from datetime import date


class MascotaFormulario(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'Dueño', 
        	'nombre', 
	        'especie', 
        	'raza' ,
        	'sexo' ,
        	'castrado',
        	'vacuna',
        	'imagen',
        	'fechaNac',

        	
        ]
        labels = {
            'Dueño': 'Dueño',
        	'nombre': 'Nombre',
	        'especie': 'Especie',
        	'raza': 'Raza',
        	'sexo': 'Sexo',
        	'castrado': 'Castrado',
        	'vacuna': 'Vacunado',
        	'imagen': 'Imagen',
        	'fechaNac': 'Fecha de Nacimiento',
	
        }
        widgets = {
            'Dueño': forms.Select(attrs={'class':'form-control'}),
        	'nombre': forms.TextInput(attrs={'class':'form-control'}),
	        'especie': forms.TextInput(attrs={'class':'form-control'}),
        	'raza': forms.TextInput(attrs={'class':'form-control'}),
        	'sexo': forms.Select(attrs={'class':'form-control'}),
        	'castrado': forms.CheckboxInput(attrs={'class':'form-control'}),
        	'vacuna': forms.CheckboxInput(attrs={'class':'form-control'}), #'vacuna': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
        	'imagen':  forms.FileInput(attrs={'class':'form-control'}),
        	'fechaNac': forms.SelectDateWidget(empty_label=("Año", "Mes", "Día"), attrs={'class':'form-control'}),
        	
        }




     