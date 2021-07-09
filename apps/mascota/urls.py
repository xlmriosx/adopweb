from django.urls import path
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('', index),
    path('nuevo_animal', mascota_view, name='crear_animal'),
    path('mascota_listado', mascota_list, name='listar_animal'),
    path('editar/<int:id_mascota>/', mascota_edit, name='editar_animal'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='eliminar_animal'),

]