# Generated by Django 4.1.1 on 2022-11-24 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_colaboradores_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaboradores',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
