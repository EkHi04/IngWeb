# Generated by Django 5.1.2 on 2024-11-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGP', '0002_rename_fecha_inicio_proyecto_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateField(),
        ),
    ]