
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

from etablissement.models import Quote

from .models import *

def pagination(request, quotes):
    # default_page 
        default_page = 1 

        page = request.GET.get('page', default_page)

        # paginate items

        items_per_page = 5

        paginator = Paginator(quotes, items_per_page)

        try:

            items_page = paginator.page(page)

        except PageNotAnInteger:

            items_page = paginator.page(default_page)

        except EmptyPage:

            items_page = paginator.page(paginator.num_pages) 

        return items_page    



def get_quote(annee:int |None = None):
    """ get quote fonction """

    obj = Quote.objects.get(annee_scolaire=annee)

    etablissements = obj.etablissement_set.all()

    context = {
        'obj': obj,
        'etablissements': etablissements
    }

    return context