from account.models import User
from anneescolaire.models import AnneeScolaire
from etablissement.models import Etablissement, Quote, get_montant_general
from django.utils import timezone
 
def run():
    etablissement = Etablissement.objects.first()
    quote = etablissement.quoteparts.first()
    
    print(quote.get_montant)
    
    