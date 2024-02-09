from django.db import models
from django.utils import timezone

# Modelos creado para obtener el mes de cumpleaños por medio de un listado.
opciones_consulta = [
    [1, "Enero"],
    [2, "Febrero"],
    [3, "Marzo"],
    [4, "Abril"],
    [5, "Mayo"],
    [6, "Junio"],
    [7, "Julio"],
    [8, "Agosto"],
    [9, "Septiembre"],
    [10, "Octubre"],
    [11, "Noviembre"],
    [12, "Diciembre"]
]

# Modelo creado para registrar los cumpleaños, dejando: nombre, apellido, dia, y mes.
class Cumpleanio(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dia = models.IntegerField()
    mes = models.IntegerField(choices=opciones_consulta)

    def __str__(self):
           return f"{self.nombre} {self.apellido} {str(self.dia)} {self.get_mes_display()}"
    
    class Meta:
        verbose_name = "Cumpleaño"
        verbose_name_plural = "Cumpleaños"