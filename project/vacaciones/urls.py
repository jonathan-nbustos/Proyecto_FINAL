from django.urls import path
from .  import views

urlpatterns = [
    path('vacaciones/', views.vacaciones, name='vacaciones'),
    path('vacaciones/list/', views.VacacionesList.as_view(), name='vacaciones_list'),
    path('vacaciones/create/', views.VacacionesCreate.as_view(), name='vacaciones_create'),
    path('vacaciones/detail/<int:pk>/', views.vacaciones_detail, name='vacaciones_detail'),
    path('vacaciones/update/<int:pk>/', views.vacaciones_update, name='vacaciones_update'),
    path('vacaciones/delete/<int:pk>/', views.vacaciones_delete, name='vacaciones_delete'),
]