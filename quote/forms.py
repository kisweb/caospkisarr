from django import forms
from etablissement.models import Etablissement, Quote


class QuoteForm(forms.ModelForm):
    
    class Meta:
        model = Quote 
        fields = (
            'etablissement',
            'annee_scolaire',
            'effectif',
            'versement',
            'montant',
            'save_by',
            'quote_date_time',
            'last_updated_date',
            'paid',
            'is_ok',
            'comments'
        )