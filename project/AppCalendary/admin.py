from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Saludo)
admin.site.register(Avatar)
admin.site.register(Contacto)