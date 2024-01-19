from account.models import User
from anneescolaire.models import AnneeScolaire
from etablissement.models import Etablissement, Quote, get_montant_general
from django.utils import timezone
from django.db.models import Avg



def run():
    annee = AnneeScolaire.objects.get(statut='anneeEnCours')
    print(get_montant_general(annee=annee, ief='Bignona1'))
    
    m = Quote.objects.aggregate(part_moyenne=Avg("versement"))
    print(m)
    print('###########')
