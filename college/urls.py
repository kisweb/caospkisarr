from django.urls import path

from . import views


app_name = 'college'


urlpatterns = [
    path('', views.colleges, name='index'),
    path('add/', views.add, name='add'),
    path('editer/<str:slug>/', views.edit, name='edit'),
    path('<str:slug>/delete/', views.delete, name='delete'),
    path('consulter/<str:slug>/', views.college, name='college'),
]