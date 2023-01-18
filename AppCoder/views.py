from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import *
from AppCoder.forms import *
from .models import *

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ferrocarril(request):
    return render(request, "AppCoder/ferrocarril.html")

def vias(request):
    return render(request, "AppCoder/vias.html")

def manodeobra(request):
    return render(request, "AppCoder/manodeobra.html")

def tables(request):
    return render(request, "AppCoder/tables.html")



def ferrocarrilFormulario(request):
    
    if request.method =="POST":

        miFormulario = FerrocarrilFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            ferrocarril = Ferrocarril(tipo=informacion["tipo"], precio=informacion["precio"])
            
            ferrocarril.save()

            return render (request, "AppCoder/inicio.html")
    
    
    
    else:

        miFormulario= FerrocarrilFormulario()
    
    return render(request, "AppCoder/ferrocarrilFormulario.html", {"miFormulario":miFormulario})



def viasFormulario(request):
    
    if request.method =="POST":

        miFormulario1 = ViasFormulario(request.POST)

        print(miFormulario1)

        if miFormulario1.is_valid:

            informacion = miFormulario1.cleaned_data

            vias = Vias(material=informacion["material"], precio=informacion["precio"])
            
            vias.save()

            return render (request, "AppCoder/inicio.html")
    
    
    
    else:

        miFormulario1= ViasFormulario()
    
    return render(request, "AppCoder/viasFormulario.html", {"miFormulario1":miFormulario1})

#calculadora

def Addition(num1,num2,num3):
    result = int(num1) + int(num2) + int(num3)
    return result
def calculadora(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        if 'add' in request.POST:
            result = Addition(num1,num2,num3)
            return render(request,'AppCoder/calculator.html',{'result':result})
    return render(request,'AppCoder/calculator.html')


def busquedaTren(request):
    return render (request, "AppCoder/busquedaTren.html")

def buscar(request):
    respuesta = f"Usted está hablando del ferrocarril modelo: {request.GET ['tipo'] }"
    return HttpResponse(respuesta)

