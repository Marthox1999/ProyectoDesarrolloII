# Generated by Django 2.2.3 on 2019-07-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20190708_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipoDocumento',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad'), ('PAS', 'Pasaporte')], max_length=3),
        ),
    ]
