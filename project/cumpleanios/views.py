from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from .  import models
from .  import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

def cumpleanio(request):
    return render(request, 'cumpleanios/cumpleanio.html')

class CumpleanioList(ListView):
    model = models.Cumpleanio
    template_name = 'cumpleanios/cumpleanio_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('consulta', '')
        if query:
            object_list = models.Cumpleanio.objects.filter(nombre__icontains=query).order_by('mes', 'dia')
        else:
            object_list = models.Cumpleanio.objects.all().order_by('mes', 'dia')
        return object_list

class CumpleanioCreate(CreateView):
    model = models.Cumpleanio
    form_class = forms.CumpleanioForm
    success_url = reverse_lazy('cumpleanios:cumpleanio_list')

class CumpleanioDetail(DetailView):
    model = models.Cumpleanio

def cumpleanio_detail(request, pk: int):
    object = models.Cumpleanio.objects.get(id=pk)
    return render(request, 'cumpleanios/cumpleanio_detail.html', {'object': object})

def cumpleanio_update(request, pk: int):
    object = models.Cumpleanio.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.CumpleanioForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('cumpleanios:cumpleanio_list')
    else:
        form = forms.CumpleanioForm(instance=object)
    return render(request, 'cumpleanios/cumpleanio_form.html', {'form': form, 'object': object})

def cumpleanio_delete(request, pk: int):
    object = models.Cumpleanio.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('cumpleanios:cumpleanio_list')
    return render(request, 'cumpleanios/cumpleanio_confirm_delete.html', {'object': object})