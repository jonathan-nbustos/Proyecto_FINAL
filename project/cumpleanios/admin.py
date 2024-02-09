from django.contrib import admin
from .models import *

# Register your models here.
admin.site_title = "Cumpleaños"

class CumpleanioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dia', 'mes')
    list_display_links = ('nombre',)
    search_fields = ('nombre', 'apellido')
    list_filter = ('mes',)
    ordering = ('mes', 'dia')

admin.site.register(Cumpleanio, CumpleanioAdmin)