from django.shortcuts import render
from django.http import HttpResponse
from apps.mascota.forms import MascotaFormulario
from apps.mascota.models import Mascota

# Create your views here.


def index(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/index.html', contexto)

def mascota_view(request): #no agrega
    if request.method =='POST':
        form = MascotaFormulario(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'mascota/index.html')
    else:
        form = MascotaFormulario()
    return render(request, 'mascota/mascota_formulario.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascota_listado.html', contexto)

def mascota_edit(request, id_mascota): #no edita
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaFormulario(instance=mascota)
    else:
        form = MascotaFormulario(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return mascota_list(request)
    return render(request, 'mascota/mascota_formulario.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return mascota_list(request)
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


