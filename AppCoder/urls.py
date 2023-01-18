from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path("ferrocarril/", views.ferrocarril, name="ferrocarril"),
    path("vias/", views.vias, name="vias"),
    path("manodeobra/", views.manodeobra, name="manodeobra"),
    path("tables.html/", views.tables, name="tables"),
    path("ferrocarrilFormulario/", views.ferrocarrilFormulario, name="FerrocarrilFormulario"),
    path("viasFormulario/", views.viasFormulario, name="viasFormulario"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("busquedaTren", views.busquedaTren, name="BusquedaCamada"),
    path("buscar/", views.buscar),

]