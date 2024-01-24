from django.shortcuts import render
from etablissement.models import Etablissement, Ief, get_montant_general, nombre_etablissement_ief
from account.models import User
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
    mesusers = User.objects.all()
    # ibou = mesusers.get('name')
    # json_object = json.dumps(employee_details, indent = 4) 
    # print(json.dumps(lesiefs, indent=4))
    print(get_montant_general())
    
    context = {
        'etablissements': mesetablissements,
        'users': mesusers,
        'iefs': Ief.objects.all(),
        'get_montant_general': get_montant_general(1)
    }
    return render(request, 'core/index.html', context=context)


def about(request):
    return render(request, 'core/about.html')


