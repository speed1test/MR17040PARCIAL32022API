# Generated by Django 4.0.5 on 2022-06-14 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='conductor',
            table='conductor',
        ),
        migrations.AlterModelTable(
            name='vehiculo',
            table='vehiculo',
        ),
    ]