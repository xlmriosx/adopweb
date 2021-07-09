from django.db import models
from django.utils import timezone
from apps.persona.models import Persona
from apps.mascota.models import Mascota

#class Publicacion(models.Model):
#	animal = OneToOneField(Mascota)
#
#	pass

class Adopcion(models.Model):
	adoptante = models.OneToOneField(Persona, on_delete=models.CASCADE)
	animal = models.OneToOneField(Mascota, on_delete=models.CASCADE)
	solicitud = models.CharField(max_length=300)
	fechaPub = models.DateField("Fecha del día de hoy", auto_now=True)
	
