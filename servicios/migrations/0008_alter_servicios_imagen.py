# Generated by Django 4.1.1 on 2022-11-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_alter_categoria_options_alter_experiencia_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(blank='True', upload_to='servicios'),
        ),
    ]
