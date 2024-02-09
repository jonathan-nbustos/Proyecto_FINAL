from django.contrib import admin
from .models import *

# Register your models here.

admin.site_title = "Vacaciones"

class VacacionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fechaInicio', 'fechaFin')
    list_display_links = ('nombre',)
    search_fields = ('apellido', )
    list_filter = ('fechaInicio', 'fechaFin', 'apellido')
    ordering = ('fechaInicio', )

admin.site.register(Vacaciones, VacacionesAdmin)