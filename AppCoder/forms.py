from django import forms

class FerrocarrilFormulario(forms.Form):

    tipo= forms.CharField()
    precio = forms.IntegerField()

class ViasFormulario(forms.Form):

    material=forms.CharField()
    precio= forms.IntegerField()
