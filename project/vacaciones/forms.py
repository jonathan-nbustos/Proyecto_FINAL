from django import forms

from . import models

class VacacionesForm(forms.ModelForm):
    class Meta:
        model = models.Vacaciones
        fields = "__all__"