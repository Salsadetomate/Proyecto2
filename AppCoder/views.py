from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ferrocarril(request):
    return render(request, "AppCoder/ferrocarril.html")

def vias(request):
    return render(request, "AppCoder/vias.html")

def manodeobra(request):
    return render(request, "AppCoder/manodeobra.html")
