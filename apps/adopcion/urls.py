from django.urls import path
from apps.adopcion.views import index, adopcion_view, adopcion_list, adopcion_edit, adopcion_delete, home_view

urlpatterns = [
    path('', home_view),
    path('nueva_adopcion', adopcion_view, name='nueva_adopcion'),
    path('listado_adopcion', adopcion_list, name='listar_adopcion'),
    #path('listado_adopcion/<int:id_mascota>', adopcion_list, name='listar_adopcion'),
    path('editar/<int:id_adopcion>/', adopcion_edit, name='editar_adopcion'),
    path('eliminar/<int:id_adopcion>/', adopcion_delete, name='eliminar_adopcion'),
]