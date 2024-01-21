from django.urls import path

from . import views


app_name = 'etablissement'


urlpatterns = [
    path('', views.etablissements, name='index'),
    path('colleges/', views.colleges, name='colleges'),
    path('lycees/', views.lycees, name='lycees'),
    path('add/', views.add, name='add'),
    path('editer/<str:slug>/', views.edit, name='edit'),
    # path('delete/<str:slug>/quote/<str:quote_id>', views.delete_quote, name='supprimerquote'),
    path('<str:slug>/delete/', views.delete, name='delete'),
    path('consulter/<str:slug>/', views.etablissement, name='etablissement'),
    path('afficher/monetablissement/', views.monEtablissement, name='monetablissement'),
]