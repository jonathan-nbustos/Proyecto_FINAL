from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Modelo creado para registrar los Saludos, dejando: nombre, apellido, mensaje y, de forma automática, la fecha de creación.
class Saludo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mensaje = models.TextField()
    fechaSaludo = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Saludo", null=True, blank=True, editable=False)
    def __str__(self):
        return self.fechaSaludo.strftime('%d/%m/%Y %H:%M') + " " + self.nombre + " " + self.apellido + " " + self.mensaje
    
    class Meta:
        verbose_name_plural = "Saludos"

# Modelo creado para crar los Avatares, dejando: usuario e imagen.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
# Modelo creado para crar los Contactos dejaendo: nombre, correo, mensaje y fecha de envio.
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre