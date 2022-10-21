from django.db import models



# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo



