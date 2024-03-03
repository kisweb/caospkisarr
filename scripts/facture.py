from account.models import User
from commande.models import Category, Beneficiaire, Order, Facture, Article
from django.utils import timezone
from pprint import pprint

def run():
    factures = Facture.objects.all()
    
    total1 = factures[0]
    pprint(total1)