from django.urls import path
from .  import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('cumpleanio/', views.cumpleanio, name='cumpleanio'),
    path('cumpleanio/list/', views.CumpleanioList.as_view(), name='cumpleanio_list'),
    path('cumpleanio/create/', views.CumpleanioCreate.as_view(), name='cumpleanio_create'),
    path('cumpleanio/detail/<int:pk>/', views.cumpleanio_detail, name='cumpleanio_detail'),
    path('cumpleanio/update/<int:pk>/', views.cumpleanio_update, name='cumpleanio_update'),
    path('cumpleanio/delete/<int:pk>/', views.cumpleanio_delete, name='cumpleanio_delete'),
]