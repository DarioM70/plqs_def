# Generated by Django 4.1.1 on 2022-11-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_colaboradores_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradores',
            name='descripcion',
            field=models.TextField(default='', max_length=500),
        ),
    ]