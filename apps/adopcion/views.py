from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.adopcion.forms import AdopcionFormulario
from apps.adopcion.models import Adopcion
from django.views.generic import ListView, CreateView
from apps.mascota.views import mascota_list
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'adopcion/index.html')

def adopcion_view(request):
    if request.method =='POST':
        form = AdopcionFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdopcionFormulario()
    return render(request, 'adopcion/adopcion_formulario.html', {'form':form})

def adopcion_list(request):
    adopcion = Adopcion.objects.all().order_by('id')
    contexto = {'adopciones': adopcion}
    return render(request, 'adopcion/adopcion_listado.html', contexto)

def adopcion_edit(request, id_adopcion): #no edita
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'GET':
        form = AdopcionFormulario(instance=adopcion)
    else:
        form = AdopcionFormulario(request.POST, instance=adopcion)
        if form.is_valid():
            form.save()
        return adopcion_list(request)
    return render(request, 'adopcion/adopcion_formulario.html', {'form':form})

def adopcion_delete(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'POST':
        adopcion.delete()
        return adopcion_list(request)
    return render(request, 'adopcion/adopcion_delete.html', {'adopcion':adopcion})

