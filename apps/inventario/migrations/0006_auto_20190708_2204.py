# Generated by Django 2.2.3 on 2019-07-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20190708_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ciudad',
            field=models.CharField(choices=[('CALI', 'Cali'), ('CUC', 'Cucuta'), ('CART', 'Cartagena'), ('BCM', 'Bucaramanga'), ('BOG', 'Bogotá'), ('SOAC', 'Soacha'), ('B/Q', 'Barranquilla'), ('SOL', 'Soledad'), ('MED', 'Medellín'), ('IBG', 'Ibague')], default='CALI', max_length=4),
        ),
    ]
