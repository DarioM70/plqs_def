from django.contrib import admin
from .models import *

# Register your models here.
class Admin_serv(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicios,Admin_serv)
admin.site.register(Categoria)
admin.site.register(Colaborador_categoria_servicio)

admin.site.register(Experiencia)
admin.site.register(Asignacion_col)
