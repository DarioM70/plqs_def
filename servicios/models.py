from django.db import models



# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=285)
    imagen = models.ImageField(upload_to='servicios', blank="True")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    categorias = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=320)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Colaborador_categoria_servicio(models.Model):
    pass

class Experiencia (models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    hoja_de_vida = models.FileField(upload_to='archivos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiancias"

    def __str__(self):
        return self.titulo

class Asignacion_col (models.Model):
    pass




