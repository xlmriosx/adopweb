from django.contrib import admin

# Register your models here.

from apps.mascota.models import Mascota, Vacuna

admin.site.register(Mascota)
admin.site.register(Vacuna)