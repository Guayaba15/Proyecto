from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def procesar_formulario(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        correo_electronico = request.POST.get('correo_electronico')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        # Guardar en la base de datos
        Mensaje.objects.create(
            nombre_completo=nombre_completo,
            correo_electronico=correo_electronico,
            asunto=asunto,
            mensaje=mensaje
        )

        return HttpResponse(f'¡Formulario enviado!<br>Nombre: {nombre_completo}<br>Correo: {correo_electronico}<br>Asunto: {asunto}<br>Mensaje: {mensaje}')

    return HttpResponse('Acceso no permitido')
