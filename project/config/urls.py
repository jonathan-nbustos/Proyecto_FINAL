from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('AppCalendary.urls','AppCalendary'))),
    path('',include(('vacaciones.urls', 'vacaciones'))),
    path('',include(('cumpleanios.urls', 'cumpleanios'))),
]