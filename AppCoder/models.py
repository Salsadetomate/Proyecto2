from django.db import models

class Ferrocarril(models.Model):

    tipo=models.CharField(max_length=50)
    precio= models.IntegerField()

class Vias(models.Model):

    material=models.CharField(max_length=50)
    precio= models.IntegerField()

class manodeobra(models.Model):

    Jefe=models.CharField(max_length=50)
    emailJefe= models.EmailField()
    Subjefe=models.CharField(max_length=50)
    emailSubjefe= models.EmailField()

