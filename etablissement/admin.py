from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Ief, Etablissement, Quote, Tresorerie

class VersementInline(GenericTabularInline):
    model = Tresorerie
    max_num = 4
    
class AdminTresorerie(admin.ModelAdmin):
    list_display = [
        'mouvement', 'montant', 'content_type', 'content_objet','object_id', 'updated_at',
    ]
    
class AdminEtablissement(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'code',
        'ief',
        'type_etablissement',        
    ]
    
    
    
class AdminQuote(admin.ModelAdmin):
    list_display = [
        'etablissement',
        'annee_scolaire',
        'effectif',
        'versement',
        'paid',
        'is_ok',
        'comments',
    ]
    inlines = [VersementInline]
    
    
admin.site.register(Ief)
admin.site.register(Etablissement, AdminEtablissement)
admin.site.register(Quote, AdminQuote)
admin.site.register(Tresorerie, AdminTresorerie)