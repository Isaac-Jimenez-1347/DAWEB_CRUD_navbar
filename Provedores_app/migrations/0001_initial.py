# Generated by Django 5.1 on 2024-11-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id_provedor', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=45)),
                ('fecha', models.CharField(max_length=30)),
                ('horarios', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('celular', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=30)),
                ('codigo_postal', models.PositiveIntegerField()),
            ],
        ),
    ]
