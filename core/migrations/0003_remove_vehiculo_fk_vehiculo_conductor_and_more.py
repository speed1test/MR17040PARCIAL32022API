# Generated by Django 4.0.5 on 2022-06-14 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_conductor_table_alter_vehiculo_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='fk_vehiculo_conductor',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='propietario',
            field=models.ForeignKey(db_column='fk_vehiculo_conductor', on_delete=django.db.models.deletion.CASCADE, to='core.conductor'),
        ),
    ]
