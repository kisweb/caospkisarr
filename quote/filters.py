import django_filters
from etablissement.models import Quote

class QuoteFilterSet(django_filters.FilterSet):
    
    class Meta:
        model = Quote
        fields = ('annee_scolaire', )