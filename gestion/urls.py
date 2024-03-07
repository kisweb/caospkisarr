from django.urls import path

from . import views


app_name = 'gestion'


urlpatterns = [
    path('', views.index, name='index'),
    path('facture/<int:pk>/imprimer/', views.facture_print, name='facture_print'),
    
]