# Generated by Django 4.1.1 on 2022-10-19 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_servicios_imagen_alter_servicios_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicios',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]