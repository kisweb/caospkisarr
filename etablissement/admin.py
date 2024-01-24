from django.contrib import admin

# Register your models here.

from .models import Etablissement, Quote


class AdminEtablissement(admin.ModelAdmin):
    list_display = (
        'slug',
        'code',
        'ief',
        'type_etablissement',
        'nomce',
        'email',
        'phone',
    )
class AdminQuote(admin.ModelAdmin):
    list_display = (
        'etablissement',
        'annee_scolaire',
        'effectif',
        'versement',
        'paid',
        'is_ok',
        'comments',
    )
    
admin.site.register(Etablissement, AdminEtablissement)
admin.site.register(Quote, AdminQuote)