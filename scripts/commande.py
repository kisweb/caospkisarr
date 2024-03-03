from account.models import User
from commande.models import Category, Beneficiaire, Order, Facture, Article
from django.utils import timezone
from pprint import pprint

def run():
    # categorie = Category()
    # categorie.name = 'Frais divers'
    # categorie.save()
    
    # pprint(categorie.slug)
    
    # produit = Product()
    # produit.category_id = 1
    # produit.name = 'Chemises à rabats'
    # produit.save()
    
    # pprint(produit.slug)
    
    orders = Order.objects.all()
    for order in orders:
        # factures = order.facture_set.all()
        pprint(order.order)
    