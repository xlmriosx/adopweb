from django.db import models
from django.utils import timezone
from apps.persona.models import Persona

class Vacuna(models.Model):
	nombre = models.CharField("Nombre de vacuna", max_length=15)
	
	def __str__(self):
		return '{}'.format(self.nombre) 


class Sexo(models.TextChoices):
    hembra = 'Hembra', ('Hembra')
    macho = 'Macho', ('Macho')


class Mascota(models.Model):
	Dueño = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=15)
	especie = models.CharField(max_length=15)
	raza = models.CharField(max_length=15)
	sexo = models.CharField(max_length=6, choices=Sexo.choices, default=Sexo.macho)
	castrado = models.BooleanField(default=False)
	vacuna = models.ManyToManyField(Vacuna)
	imagen = models.ImageField(upload_to="")
	fechaNac = models.DateField("Fecha de nacimiento")
	fechaPub = models.DateField("Fecha del día de hoy", auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.especie) 


	

# id = models.AutoField(primary_key=True)
# duenio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title