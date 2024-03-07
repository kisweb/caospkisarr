from django.shortcuts import render, reverse, redirect
from django.contrib import messages
import datetime
from .models import Commande, Personne, Facture
from .forms import *

def index(request):
    
    context = {
        'segment': 'gestion-index', 
        'ladate': datetime.datetime.today(),
        'beneficiaires': Personne.objects.filter(personne_type='BENEFICIAIRE').count(),
        'fournisseurs': Personne.objects.filter(personne_type='FOURNISSEUR').count(),
        'commandes': Commande.objects.count(),
        'factures': Facture.objects.all(),
    }

    return render(request, 'gestion/index.html', context=context)

def facture_print(request, pk):
    facture = Facture.objects.get(id=pk)
    
    context = {
        'segment': 'gestion-facture-print', 
        'ladate': datetime.datetime.today(), 
        'facture': facture, 
        'partenaires': Personne.objects.all(),
    }

    return render(request, 'gestion/facture.html', context=context)