from django.urls import path

from . import views


app_name = 'commande'


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category, name='category'),
    path('beneficiaires/', views.beneficiaire, name='beneficiaire'),
    path('nouvelle/', views.order, name='order'),
    path('gestion-commandes/articles/', views.article, name='article'),
    path('gestion-commandes/factures/ajouter/', views.facture_add, name='facture_add'),
    path('gestion-commandes/facture/<int:pk>/imprimer/', views.facture_print, name='facture_print'),
    
]