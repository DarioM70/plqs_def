# Generated by Django 4.1.1 on 2022-11-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0008_alter_servicios_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]