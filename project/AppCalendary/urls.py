from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

# Para las imagenes:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', TemplateView.as_view(template_name='AppCalendary/about.html'), name='about'),
    path('contacto/', views.contacto, name='contacto'),

    path('saludo/', views.saludo, name='saludo'),
    path('saludo/list/', views.SaludoList.as_view(), name='saludo_list'),
    path('saludo/create/', views.SaludoCreate.as_view(), name='saludo_create'),
    path('saludo/detail/<int:pk>/', views.saludo_detail, name='saludo_detail'),
    path('saludo/update/<int:pk>/', views.saludo_update, name='saludo_update'),    
    path('saludo/delete/<int:pk>/', views.saludo_delete, name='saludo_delete'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="AppCalendary/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('CambiarContrasenia/', views.CambiarContrasenia.as_view(), name='CambiarContrasenia'),

    #path('saludo/list/', views.saludo_list, name='saludo_list'),
    # path('saludo/create/', views.saludo_create, name='saludo_create'),
    # path('saludo/detail/<int:pk>/', views.SaludoDetail.as_view(), name='saludo_detail'),
    # path('saludo/update/<int:pk>/', views.SaludoUpdate.as_view(), name='saludo_update'),
    # path('saludo/delete/<int:pk>/', views.SaludoDelete.as_view(), name='saludo_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)