# Generated by Django 3.2.4 on 2021-07-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARRITO', '0003_auto_20210706_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'verbose_name': 'Carrito'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='producto',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
