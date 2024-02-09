from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from .  import models
from .  import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
def vacaciones(request):
    return render(request, 'vacaciones/vacaciones.html')

class VacacionesList(ListView):
    model = models.Vacaciones
    objects = models.Vacaciones.objects.all()
    contexto = {'object_list': objects}

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = VacacionesList.objects.filter(nombre__icontains=consulta)
        else:
            object_list = VacacionesList.objects.all()
        return object_list


class VacacionesCreate(CreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    success_url = reverse_lazy('vacaciones:vacaciones_list')

class VacacionesDetail(DetailView):
    model = models.Vacaciones

def vacaciones_detail(request, pk: int):
    object = models.Vacaciones.objects.get(id=pk)
    return render(request, 'vacaciones/vacaciones_detail.html', {'object': object})

def vacaciones_update(request, pk: int):
    object = models.Vacaciones.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.VacacionesForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('vacaciones:vacaciones_list')
    else:
        form = forms.VacacionesForm(instance=object)
    return render(request, 'vacaciones/vacaciones_form.html', {'form': form, 'object': object})

def vacaciones_delete(request, pk: int):
    object = models.Vacaciones.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('vacaciones:vacaciones_list')
    return render(request, 'vacaciones/vacaciones_confirm_delete.html', {'object': object})