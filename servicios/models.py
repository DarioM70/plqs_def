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

class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)

class Colaborador_categoria_servicio(models.Model):
    pass

class Experiencia (models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    hoja_de_vida = models.FileField(upload_to='archivos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo

class Asignacion_col (models.Model):
    pass




