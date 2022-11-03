from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=250, null=False, blank=False)
    segundoNombre = models.CharField(max_length=250)
    primerApellido = models.CharField(max_length=250, null=False, blank=False)
    segundoApellido = models.CharField(max_length=250)
    descripción = models.TextField(blank=False, null=False)