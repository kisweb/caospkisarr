from account.models import User
from anneescolaire.models import AnneeScolaire
from etablissement.models import Etablissement, Quote, get_montant_general
from django.utils import timezone
from pprint import pprint

def run():
    etablissement = Etablissement.objects.first()
    quote = etablissement.quotes.all()
    
    pprint(quote.first().get_montant)
    
    