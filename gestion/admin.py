from django.contrib import admin

from .models import Personne, Commande, CommandeArticle, Facture, Depense
from account.models import User

class CommandeArticleInline(admin.TabularInline):
    model = CommandeArticle
    max_num = 10

class AdminPersonne(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'personne_type')
    
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('fournisseur', 'complete', 'transaction_id', 'status')
    inlines = [CommandeArticleInline]
    
    
class AdminFacture(admin.ModelAdmin):
    list_display = ('commande', 'facture_type', 'beneficiaire', 'get_montant_net')
    
    
class AdminDepense(admin.ModelAdmin):
    list_display = [
        'mouvement', 'montant', 'content_type', 'content_objet','object_id', 'updated_at',
    ]


admin.site.register(Commande, AdminCommande)
admin.site.register(Personne, AdminPersonne)
admin.site.register(Facture, AdminFacture)
admin.site.register(Depense, AdminDepense)