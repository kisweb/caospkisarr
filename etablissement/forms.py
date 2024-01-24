from django import forms
from anneescolaire.models import AnneeScolaire

from etablissement.models import Ief, Quote, Etablissement

class FilterQuoteAnneeForm(forms.ModelForm):
    quote_annee = forms.ModelChoiceField(
        queryset=AnneeScolaire.objects.all(),
    )
    class Meta:
        model = AnneeScolaire
        fields = ('id', 'annee')
    
    
    
class FilterIefForm(forms.ModelForm):
    iefs = forms.ModelChoiceField(
        queryset=Ief.objects.all(),
    )
    class Meta:
        model = Ief
        fields = ('id', 'name')
    


class FilterTypeEtablissementForm(forms.Form):
    type_etablissement = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=Etablissement.TypeEtablissement.choices
    )
    
class EtablissementCreateForm(forms.ModelForm):
    # ief = forms.ModelChoiceField(
    #     queryset=Ief.objects.filter(slug__in=['bignona-1', 'bignona-2'])
    # )
    class Meta:
        model = Etablissement
        fields = ('name', 'ief', 'type_etablissement', 'nomce', 'email', 'phone', 'address')