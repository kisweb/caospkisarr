from django.shortcuts import render
from etablissement.models import Etablissement, Ief, get_montant_general
from anneescolaire.models import AnneeScolaire
from account.models import User
from gestion.models import get_depense_general
import json
from login_required import login_not_required


@login_not_required
def home(request):
    pass


def dashboard(request):
    pass


def index(request):
    # lesresp = Ief.objects.values_list('conseiller', flat=True).distinct()  # returns a list of tuples..
    mesetablissements = Etablissement.objects.all()
    etablissement = mesetablissements.filter(code=request.user.profile.code_etablissement).first()
    mesusers = User.objects.all()
    # ibou = mesusers.get('name')
    # json_object = json.dumps(employee_details, indent = 4) 
    # print(json.dumps(lesiefs, indent=4))
    print(get_montant_general())
    
    context = {
        'etablissements': mesetablissements,
        'etablissement': etablissement,
        'users': mesusers,
        'iefs': Ief.objects.all(),
        'get_montant_general': get_montant_general,
        'get_depense_general': get_depense_general,
    }
    return render(request, 'core/index.html', context=context)


def about(request):
    return render(request, 'core/about.html')

def term(request):
    return render(request, 'core/term.html')


