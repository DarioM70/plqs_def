from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=100, blank=False)
    segundoNombre = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100, blank=False)
    segundoApellido = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, blank=False, default='')
    foto = models.ImageField(upload_to='servicios', blank="True")


    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.primerNombre