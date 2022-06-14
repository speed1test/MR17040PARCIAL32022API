from django.db import models

class Conductor(models.Model):
    licencia = models.CharField(max_length=20, primary_key=True, null = False)
    nombre = models.CharField(max_length=100, null = False)
    edad = models.IntegerField()
    estado_civil = models.CharField(max_length=50)
    tipo_licencia = models.CharField(max_length=20, null = False)
    class Meta:
        db_table = 'conductor'

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=10, primary_key=True, null = False)
    propietario = models.ForeignKey(Conductor, on_delete=models.CASCADE, db_column="fk_vehiculo_conductor")
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    #fk_vehiculo_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'vehiculo'