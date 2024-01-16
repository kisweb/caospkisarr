from django.urls import path

from . import views


app_name = 'ief'


urlpatterns = [
    path('', views.iefs, name='index'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.ief, name='ief'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
]