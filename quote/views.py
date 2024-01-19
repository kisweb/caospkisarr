from django.shortcuts import render
from django.views import View
from etablissement.models import Etablissement, Quote, get_montant_general
from etablissement.forms import FilterQuoteAnneeForm
from django.contrib import messages

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

    quotes = Quote.objects.all().order_by('-quote_date_time')
    
    context = {
        'quotes': quotes
    }

    def get(self, request, *args, **kwags):
 
        items = pagination(request, self.quotes)
        if request.GET.get('quote_annee') == "ALL" or request.GET.get('quote_annee') is None:
            quote_qs = self.quotes.all()
        else:
            quote_annees = request.GET.getlist('quote_annee')
            quote_qs = self.quotes.filter(annee_scolaire__in=quote_annees)

        context = {'quotes': quote_qs.order_by('annee_scolaire', 'etablissement'), 'form': FilterQuoteAnneeForm(), 'annees': ANNEES}

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

    quotes = Quote.objects.select_related('save_by').all()

    context = {
        'quotes': quotes
    }

    def get(self, request, *args, **kwargs):
        return  render(request, self.template_name, self.context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        
        try: 
            etablissement = request.POST.get('etablissement')
            annee = request.POST.get('annee_scolaire')
            versement = request.POST.get('versement')
            effectif = request.POST.get('effectif')
            quote_date_time = request.POST.get('quote_date_time')
            montant = self.get_montant()
            comments = request.POST.get('comments')
             
            quote_object = {
                'etablissement': etablissement,
                'annee_scolaire': annee,
                'versement': versement,
                'effectif': effectif,
                'save_by': request.user,
                'quote_date_time': quote_date_time,
                'montant': montant,
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

    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        context = get_quote(pk)

        return render(request, self.template_name, context)


@superuser_required
def get_quote_pdf(request, *args, **kwargs):
    """ generate pdf file from html file """

    pk = kwargs.get('pk')

    context = get_quote(pk)

    context['date'] = datetime.datetime.today()

    # get html file
    template = get_template('quote_part/quote-pdf.html')

    # render html with context variables

    html = template.render(context)

    # options of pdf format 

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": ""
    }

    # generate pdf 

    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = "attachement"

    return response



