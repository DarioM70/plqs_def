# Generated by Django 4.1.1 on 2022-11-12 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_alter_categoria_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='experiencia',
            options={'verbose_name': 'Experiencia', 'verbose_name_plural': 'Experiancias'},
        ),
        migrations.RenameField(
            model_name='servicios',
            old_name='contenido',
            new_name='descripcion',
        ),
    ]
