import django_filters
from etablissement.models import Etablissement

class EtablissementFilterSet(django_filters.FilterSet):
    
    class Meta:
        model = Etablissement
        fields = ('type_etablissement',)