# Generated by Django 4.1.1 on 2022-10-24 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_asignacion_col_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]