from django import forms

from etablissement.models import Ief, Quote, Etablissement

class FilterQuoteAnneeForm(forms.Form):
    quote_annee = forms.ChoiceField(
        # widget=forms.CheckboxSelectMultiple,
        choices=Quote.QuoteAnneeScolaires.choices
    )
class FilterIefForm(forms.Form):
    pass
class FilterTypeEtablissementForm(forms.Form):
    type_etablissement = forms.ChoiceField(
        #widget=forms.CheckboxSelectMultiple,
        choices=Etablissement.TypeEtablissement.choices
    )
    
class EtablissementCreateForm(forms.ModelForm):
    # ief = forms.ModelChoiceField(
    #     queryset=Ief.objects.filter(slug__in=['bignona-1', 'bignona-2'])
    # )
    class Meta:
        model = Etablissement
        fields = ('name', 'ief', 'type_etablissement', 'nomce', 'email', 'phone', 'address')