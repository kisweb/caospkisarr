from django.contrib import admin

# Register your models here.

from .models import AnneeScolaire
        
class AdminAnneeScolaire(admin.ModelAdmin):
    list_display = ('annee', 'active', 'statut')
    
admin.site.register(AnneeScolaire, AdminAnneeScolaire)