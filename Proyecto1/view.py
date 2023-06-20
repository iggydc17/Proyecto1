import datetime
from django.http import HttpResponse
from django.template import loader


def saludo(request):
    return HttpResponse("Hola Django-Coder.")

def segundo_saludo(request):
    return HttpResponse('<br><br> <h1>Hola mundo! </h1>.')

def diaDeHoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es el día <br> {dia}"
    return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):
    data = f'Mi nombre es: <h1>{nombre}</h1>'
    return HttpResponse(data)

def probandoTemplate(self):

    nombre = 'Ignacio'
    apellido = 'Gonzalez'

    namelist = ['Gabriel', 'Jimena', 'Ignacio', 'Patricia', 'Natalia']

    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'namelist': namelist
    }

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)