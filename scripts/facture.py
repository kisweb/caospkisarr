from account.models import User
from gestion.models import Commande, Facture, CommandeArticle
from django.utils import timezone
from pprint import pprint

def run():
    facture = Facture.objects.get(id=1)
    
    fact = facture
    pprint(fact)