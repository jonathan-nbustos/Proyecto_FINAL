from django import forms

from . import models

class CumpleanioForm(forms.ModelForm):
    class Meta:
        model = models.Cumpleanio
        fields = "__all__"