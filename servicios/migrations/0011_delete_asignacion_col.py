# Generated by Django 4.1.1 on 2022-11-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0010_delete_categoria_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Asignacion_col',
        ),
    ]