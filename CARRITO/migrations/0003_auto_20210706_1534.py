# Generated by Django 3.2.4 on 2021-07-06 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CARRITO', '0002_auto_20210706_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={},
        ),
        migrations.RenameField(
            model_name='carrito',
            old_name='listaProductos',
            new_name='productos',
        ),
    ]
