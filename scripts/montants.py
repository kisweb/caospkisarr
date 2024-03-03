from account.models import User
from anneescolaire.models import AnneeScolaire
from etablissement.models import Etablissement, Quote, get_montant_general
from django.utils import timezone
from django.db.models import Avg
from pprint import pprint



def run():
    annee = AnneeScolaire.objects.get(statut='anneeEnCours')
    pprint(get_montant_general())
    
    m = Quote.objects.aggregate(part_moyenne=Avg("versement"))
    pprint(m)
    pprint('###########')
