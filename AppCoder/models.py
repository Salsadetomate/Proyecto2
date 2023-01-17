from django.db import models

class ferrocarril(models.Model):

    tipo=models.CharField(max_length=50)
    precio= models.IntegerField()

class vias(models.Model):

    material=models.CharField(max_length=50)
    precio= models.IntegerField()

class manodeobra(models.Model):

    Jefe=models.CharField(max_length=50)
    emailJefe= models.EmailField()
    Subjefe=models.CharField(max_length=50)
    emailSubjefe= models.EmailField()

