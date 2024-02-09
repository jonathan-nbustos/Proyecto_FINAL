from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


from .  import models
from .  import forms

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

def index(request):
    return render(request, 'AppCalendary/index.html')

def saludo(request):
    return render(request, 'AppCalendary/saludo.html')

def contacto(request):
    data = {'form': forms.ContactoForm()}
    if request.method == 'POST':
        formulario = forms.ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El mensaje fue enviado. Muchas gracias!"
        else:
            data["form"] = formulario
    return render(request, 'AppCalendary/contacto.html', data)

# List
# def saludo_list(request):
#     objects = models.Saludo.objects.all()
#     contexto = {'object_list': objects}
#     return render(request, 'AppCalendary/saludo_list.html', contexto)


# def saludo_create(request):
#     if request.method == 'POST':
#         form = forms.SaludoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('AppCalendary:saludo_list')
#     else: #request.method == 'GET':
#         form = forms.SaludoForm()
#     return render(request, 'AppCalendary/saludo_create.html', {'form': form})

class SaludoList(ListView):
    model = models.Saludo
    objects = models.Saludo.objects.all()
    contexto = {'object_list': objects}

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = SaludoList.objects.filter(nombre__icontains=consulta)
        else:
            object_list = SaludoList.objects.all()
        return object_list

class SaludoCreate(CreateView):
    model = models.Saludo
    form_class = forms.SaludoForm
    success_url = reverse_lazy('AppCalendary:saludo_list')

class SaludoDetail(DetailView):
    model = models.Saludo

def saludo_detail(request, pk: int):
    object = models.Saludo.objects.get(id=pk)
    return render(request, 'AppCalendary/saludo_detail.html', {'object': object})

# class SaludoUpdate(UpdateView):
#     model = models.Saludo
#     form_class = forms.SaludoForm
#     success_url = reverse_lazy('AppCalendary:saludo_list')
    
def saludo_update(request, pk: int):
    object = models.Saludo.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.SaludoForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('AppCalendary:saludo_list')
    else:
        form = forms.SaludoForm(instance=object)
    return render(request, 'AppCalendary/saludo_form.html', {'form': form, 'object': object})

# class SaludoDelete(DeleteView):
#     model = models.Saludo
#     success_url = reverse_lazy('AppCalendary:saludo_list')

def saludo_delete(request, pk: int):
    object = models.Saludo.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('AppCalendary:saludo_list')
    return render(request, 'AppCalendary/saludo_confirm_delete.html', {'object': object})

class CustomLoginView(LoginView):
    authentication_form = forms.CustomAuthenticationForm
    template_name = "AppCalendary/login.html"

def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCalendary:login')
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "AppCalendary/register.html", {"form": form})

# def editar_perfil(request):
#     usuario = request.user
#     if request.method == 'POST':
#         form = forms.UserEditForm(request.POST,request.FILES, instance=request.user)
#         if form.is_valid():
#             if form.cleaned_data.get('imagen'):
#                 usuario.avatar.imagen = form.cleaned_data.get('imagen')
#                 usuario.avatar.save()
#             form.save()
#             return render(request, "AppCalendary/index.html")
#     else:
#         form = forms.UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
#     return render(request, "AppCalendary/editar_perfil.html", {"form": form, "usuario": usuario})

def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if not hasattr(usuario, 'avatar') and form.cleaned_data.get('imagen'):
                # Si el usuario no tiene un avatar, crea uno
                avatar = models.Avatar.objects.create(user=usuario, imagen=form.cleaned_data.get('imagen'))
            elif hasattr(usuario, 'avatar') and form.cleaned_data.get('imagen'):
                # Si el usuario ya tiene un avatar, actualiza la imagen del avatar existente
                usuario.avatar.imagen = form.cleaned_data.get('imagen')
                usuario.avatar.save()
            form.save()
            return render(request, "AppCalendary/index.html")
    else:
        initial_data = {'imagen': usuario.avatar.imagen} if hasattr(usuario, 'avatar') else {}
        form = forms.UserEditForm(initial=initial_data, instance=request.user)
    return render(request, "AppCalendary/editar_perfil.html", {"form": form, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppCalendary/cambiar_contrasenia.html"
    success_url = reverse_lazy('AppCalendary:editar_perfil')