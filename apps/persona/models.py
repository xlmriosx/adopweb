from django.db import models
from django.utils import timezone
 

class Comunicacion(models.TextChoices):
    celular = 'Cel', ('Celular')
    telefono = 'Tel', ('Telefono')

class Persona(models.Model):
	nombre = models.CharField(max_length=15, default='')
	apellido = models.CharField(max_length=15, default='')
	email = models.EmailField(default='')
	fechaNac = models.DateField("Fecha de nacimiento", null=True)
	fechaRegistro = models.DateField("Fecha del día de hoy", auto_now=True)
	telcel = models.CharField("Telefono o Celular", max_length=3, choices=Comunicacion.choices, default=Comunicacion.telefono)
	numero = models.IntegerField(default=3624)
	denuncias = models.TextField()
	pass

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido) 

