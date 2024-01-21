from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Etablissement, Quote


class AdminEtablissement(ImportExportModelAdmin):
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