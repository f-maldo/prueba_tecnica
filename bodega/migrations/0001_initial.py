# Generated by Django 3.0.7 on 2020-06-21 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=45)),
                ('estado_producto', models.CharField(max_length=45)),
            ],
        ),
    ]