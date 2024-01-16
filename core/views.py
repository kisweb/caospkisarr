from django.shortcuts import render
from ief.models import Ief
from college.models import College, get_montant_general
from account.models import User
import json
from login_required import login_not_required


@login_not_required
def home(request):
    pass


def dashboard(request):
    pass


def index(request):
    lesiefs = Ief.objects.values_list('name', flat=True).distinct()  # returns a list of tuples..
    # lesresp = Ief.objects.values_list('conseiller', flat=True).distinct()  # returns a list of tuples..
    mesiefs = Ief.objects.order_by('name').all()
    mescolleges = College.objects.all()
    mesusers = User.objects.all()
    # ibou = mesusers.get('name')
    # json_object = json.dumps(employee_details, indent = 4) 
    # print(json.dumps(lesiefs, indent=4))
    print(get_montant_general())
    
    context = {
        'iefs': mesiefs,
        'colleges': mescolleges,
        'users': mesusers,
        'lesiefs': lesiefs,
        'montant_total': get_montant_general()
    }
    return render(request, 'core/index.html', context=context)


def about(request):
    return render(request, 'core/about.html')


