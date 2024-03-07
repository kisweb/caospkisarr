from django import forms
from anneescolaire.models import AnneeScolaire

from gestion.models import Commande, Personne, CommandeArticle, Facture


class PersonneCreateForm(forms.ModelForm):    
    class Meta:
        model = Personne
        fields = ('name', 'personne_type', 'piece', 'numero', 'service', 'address', 'phone', 'locality')
  