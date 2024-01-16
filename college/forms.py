from django import forms

from college.models import Quote

class FilterQuoteAnneeForm(forms.Form):
    quote_annee = forms.ChoiceField(
        # widget=forms.CheckboxSelectMultiple,
        choices=Quote.QuoteAnneeScolaires.choices
    )