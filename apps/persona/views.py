from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from apps.persona.forms import PersonaFormulario, RegistroFormulario 
from apps.persona.models import Persona
from django.core import serializers
#from django.core.urlresolvers import reverse_lazy
# Create your views here.


def index(request):
    persona = Persona.objects.all().order_by('id')
    contexto = {'personas': persona}
    return render(request, 'persona/index.html', contexto)

def persona_view(request): #no agrega
    if request.method =='POST':
        form = PersonaFormulario(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'persona/index.html')
    else:
        form = PersonaFormulario()
    return render(request, 'persona/persona_formulario.html', {'form':form})

def persona_list(request):
    persona = Persona.objects.all().order_by('id')
    contexto = {'personas': persona}
    return render(request, 'persona/persona_listado.html', contexto)

def persona_edit(request, id_persona): #no edita
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'GET':
        form = PersonaFormulario(instance=persona)
    else:
        form = PersonaFormulario(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return persona_list(request)
    return render(request, 'persona/persona_formulario.html', {'form':form})

def persona_delete(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'POST':
        persona.delete()
        return persona_list(request)
    return render(request, 'persona/persona_delete.html', {'persona':persona})

def persona_denunciar(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'GET':
        form = PersonaFormulario(instance=persona)
    else:
        form = PersonaFormulario(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return denuncia_list(request) #muestro esto despues de denunciar
    return render(request, 'persona/persona_denunciar.html', {'form':form})

class RegistroUsuario(CreateView):
    model = User
    template_name = 'persona/registrar_persona.html'
    form_class = RegistroFormulario
    success_url = 'persona_listado'

def denuncia_list(request):
    persona = Persona.objects.all().order_by('id')
    contexto = {'personas': persona}
    return render(request, 'persona/denuncia_listado.html', contexto)

def denuncia(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    form = PersonaFormulario(instance=persona)
         #muestro esto despues de denunciar
    return render(request, 'persona/denuncias.html', {'form':form})




