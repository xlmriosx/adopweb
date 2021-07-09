from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.persona.views import denuncia, denuncia_list, index, persona_denunciar, persona_view, persona_list, persona_edit, persona_delete, RegistroUsuario
#from django.contrib.auth.decorators import 

LogoutView.template_name='persona/cerrar_persona.html'


urlpatterns = [
    path('', index),
    path('nueva_persona', persona_view, name='nueva_persona'),
    path('persona_listado', persona_list, name='listar_persona'),
    path('editar/<int:id_persona>/', persona_edit, name='editar_persona'),
    path('eliminar/<int:id_persona>/', persona_delete, name='eliminar_persona'),
    path('registrar_usuario', RegistroUsuario.as_view(), name='registrar_persona'),
    path('persona_denunciar/<int:id_persona>', persona_denunciar, name='persona_denunciar'),
    path('denuncia_listado', denuncia_list, name='denuncia_listado' ),
    path('denuncia_listado/<int:id_persona>', denuncia, name='denuncia'),

]
