# Generated by Django 4.0.4 on 2022-07-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0011_remove_producto_nombre_foto_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default='Sin_imagen', max_length=50),
        ),
    ]
