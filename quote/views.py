from django.shortcuts import render, reverse
from django.views import View
from etablissement.models import Etablissement, Quote, get_montant_general
from quote.filters import QuoteFilterSet
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse

import pdfkit

import datetime
from helpers.util import *

from django.template.loader import get_template

from django.db import transaction

from .utils import pagination, get_quote

from .decorators import *
from caosp.settings import ANNEES

from django.utils.translation import gettext as _
"""
etablissement
annee_scolaire
effectif
versement
montant
save_by
quote_date_time
last_updated_date
paid
is_ok
comments
"""

# Create your views here.

class QuoteView(LoginRequiredSuperuserMixim,View):
    """ Main view """

    templates_name = 'quote_part/index.html'   

    def get(self, request, *args, **kwags):
        filterset = QuoteFilterSet(request.GET, queryset=Quote.objects.prefetch_related("annee_scolaire", "etablissement"))
        lesquotes = filterset.qs
        page_num = request.GET.get('page', 1)
        per_page = int(request.GET.get('per_page', 3))
        paginator = Paginator(lesquotes, per_page)
        
        try:
            lesquotes = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            lesquotes = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            lesquotes = paginator.page(paginator.num_pages)
        
        context = {'segment': 'quote-list', 'quotes': lesquotes, 'filter': filterset, 'montantTotal': get_montant_general(int(request.GET.get('quote_annee') or 1))}

        return render(request, self.templates_name, context=context)


    def post(self, request, *args, **kwagrs):

        # modify an quote

        if request.POST.get('id_modified'):

            paid = request.POST.get('modified')

            try: 

                obj = Quote.objects.get(id=request.POST.get('id_modified'))

                if paid == 'True':

                    obj.paid = True

                else:

                    obj.paid = False 

                obj.save() 

                messages.success(request,  _("Change made successfully.")) 

            except Exception as e:   

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        # deleting an quote    

        if request.POST.get('id_supprimer'):

            try:

                obj = Quote.objects.get(pk=request.POST.get('id_supprimer'))

                obj.delete()

                messages.success(request, _("The deletion was successful."))   

            except Exception as e:

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        items = pagination(request, self.quotes)

        self.context['quotes'] = items

        return render(request, self.templates_name, self.context)    


class AddEtablissementView(LoginRequiredSuperuserMixim, View):
     """ add new etablissement """    
     template_name = 'quote_part/add_etablissement.html'

     def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

     def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'address': request.POST.get('address'),
            'ief': request.POST.get('ief'),
            'code': h_random_ascii(8),
            'save_by': request.user

        }

        try:
            created = Etablissement.objects.create(**data)

            if created:

                messages.success(request, "Etablissement registered successfully.")

            else:

                messages.error(request, "Sorry, please try again the sent data is corrupt.")

        except Exception as e:    

            messages.error(request, f"Sorry our system is detecting the following issues {e}.")

        return render(request, self.template_name)   



class AddQuoteView(LoginRequiredSuperuserMixim, View):
    """ add a new quote view """

    template_name = 'quote_part/add_quote.html'

    quotes = Quote.objects.all()

    context = {
        'quotes': quotes
    }

    def get(self, request, *args, **kwargs):
        return  render(request, self.template_name, self.context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        
        try: 
            etablissement_id = request.POST.get('etablissement_id')
            annee_id = request.POST.get('annee_id')
            versement = request.POST.get('versement')
            effectif = request.POST.get('effectif')
            comments = request.POST.get('comments')
            user_id = request.POST.get('user_id')
             
            quote_object = {
                'etablissement_id': etablissement_id,
                'annee_scolaire_id': annee_id,
                'versement': versement,
                'effectif': effectif,
                'save_by_id': user_id,
                'comments': comments
            }

            quote = Quote.objects.create(**quote_object)               

            if quote:
                messages.success(request, "Data saved successfully.") 
            else:
                messages.error(request, "Sorry, please try again the sent data is corrupt.")    

        except Exception as e:
            messages.error(request, f"Sorry the following error has occured {e}.")   

        return  render(request, self.template_name, self.context)


class QuoteVisualizationView(LoginRequiredSuperuserMixim, View):
    """ This view helps to visualize the quote """

    template_name = 'quote_part/quote.html'

    def get(self, request):

        quotes = get_quote(annee=1)

        context = {'quotes': quotes}
        return render(request, self.template_name, context)

def voir_quotes(request):
    annee = request.GET.get('quote_annee')
    quotes = QuoteFilterSet(request.GET, queryset=Quote.objects.prefetch_related('annee_scolaire', 'etablissement'))
    
    return render(request, 'quote_part/quote.html', {
        'quotes': quotes.qs,
        'ladate': datetime.datetime.today(),
        'periode': int(request.GET.get('annee_scolaire')),
        'filter': QuoteFilterSet,
        'segment': 'quote-list',
        'montantTotal': get_montant_general(int(request.GET.get('annee_scolaire', 1)))

    })

