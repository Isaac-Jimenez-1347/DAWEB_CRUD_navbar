# Generated by Django 5.1 on 2024-11-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('ubicacion', models.CharField(max_length=30)),
                ('horarios', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=30)),
                ('celular', models.PositiveIntegerField()),
                ('id_empleado', models.CharField(max_length=11)),
            ],
        ),
    ]
