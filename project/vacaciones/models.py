from django.db import models
from django.utils import timezone

# Modelo creado para registrar los vacaciones, dejando: nombre, apellido, fecha de inicio y fecha de fin.
class Vacaciones(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaInicio = models.DateField(verbose_name="Fecha de inicio")
    fechaFin = models.DateField(verbose_name="Fecha de fin")

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.fechaInicio) + " " + str(self.fechaFin)
    
    class Meta:
        verbose_name_plural = "Vacaciones"