from django import forms

from etablissement.models import Quote, Etablissement

class FilterQuoteAnneeForm(forms.Form):
    quote_annee = forms.ChoiceField(
        # widget=forms.CheckboxSelectMultiple,
        choices=Quote.QuoteAnneeScolaires.choices
    )
class FilterIefForm(forms.Form):
    ief = forms.ChoiceField(
        #widget=forms.ChoiceField,
        choices=Etablissement.IEF
    )
class FilterTypeEtablissementForm(forms.Form):
    type_etablissement = forms.ChoiceField(
        #widget=forms.CheckboxSelectMultiple,
        choices=Etablissement.TypeEtablissement.choices
    )