from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio),
    path("ferrocarril/", views.ferrocarril, name="Ferrocarril"),
    path("vias/", views.vias),
    path("manodeobra/", views.manodeobra),

]