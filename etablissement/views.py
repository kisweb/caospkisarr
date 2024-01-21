from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
from django.db.models import Subquery, OuterRef
from anneescolaire.models import AnneeScolaire

from quote.decorators import superuser_required
from login_required import login_not_required
from .models import Etablissement, Quote
from account.models import User
from caosp.settings import ANNEES
from helpers.util import *
from etablissement.forms import FilterQuoteAnneeForm, FilterIefForm,FilterTypeEtablissementForm

from caosp.utils import unique_slug_generator


def etablissements(request):
    # last_year = datetime.now() - timedelta(days=365)
    # Using Subquery
    # recent_etablissements = Etablissement.objects.filter(created_date__gte=last_year)
    
    # authors_with_recent_books = Author.objects.filter(id__in=Subquery(recent_books.values('author_id')))

    lesetabs = Etablissement.objects.all().order_by('id')
    page_num = request.GET.get('page', 1)
    per_page = int(request.GET.get('per_page', 10))
    paginator = Paginator(lesetabs, per_page) # 10 établissement per page


    try:
        etablissements = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        etablissements = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        etablissements = paginator.page(paginator.num_pages)
        
    return render(request, 'etablissement/etablissements.html', {
        'etablissements': etablissements,
        'segment': 'etablissement-list'

    })


def colleges(request):
    etablissements = Etablissement.objects.filter(type_etablissement='Collège').all()
    return render(request, 'etablissement/etablissements.html', {
        'etablissements': etablissements,
        'segment': 'etablissement-list'

    })


def lycees(request):
    etablissements = Etablissement.objects.filter(type_etablissement = 'Lycée')
    return render(request, 'etablissement/etablissements.html', {
        'etablissements': etablissements,
        'segment': 'etablissement-list'

    })


def etablissement(request, slug):
    # quotes = Quote.select_related('etablissement', 'save_by').get(etablissement=pk)
    etablissement = Etablissement.objects.get(slug=slug)
    form = FilterQuoteAnneeForm()
    print(etablissement)
    if request.POST.get('id_supprimer') == "yes":
        etablissement.delete()
        messages.success(request,  f"Toutes les données de '{etablissement.name}' ont été supprimées.") 
        return redirect(f'/etablissements/')
        
    return render(request, 'etablissement/etablissement.html', {
        'etablissement': etablissement,
        'annees': ANNEES
    })


def monEtablissement(request):
    # quotes = Quote.select_related('etablissement', 'save_by').get(etablissement=pk)
    mail = request.user.email.split('@')[0]
    # email = mail+'@caosp.zig'
    # print(mail)
    if Etablissement.objects.get(slug=mail).exists():
        
        messages.success(request,  f"Les données de '{etablissement.name}' ne peuvent être affichées.")
    
        return render(request, 'etablissements.html')
    
    context = {
        'etablissement': etablissement,
        'annees': ANNEES        
    }
    return redirect(f'/etablissement/{mail}', context=context)
    

def add(request):
    lesusers = User.objects.all()
    types = FilterTypeEtablissementForm()
    iefs = FilterIefForm()
    print(iefs)
    if request.method == 'POST':
        
        name = request.POST.get('name')
        slug = unique_slug_generator(request.POST.get('name'))
        type_etablissement = request.POST.get('type_etablissement')
        address = request.POST.get('address')
        ief = request.POST.get('ief')
        nomce = request.POST.get('nomce')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        print(request.POST)
        if etablissement:
            Etablissement.objects.create(
                code=h_random_ascii(6), 
                name=name,
                slug=slug,
                email=email, 
                ief=ief,
                type_etablissement=type_etablissement,
                address=address,
                nomce=nomce, 
                phone=phone, 
                save_by=request.user
            )
    context = {'segment': 'etablissement-add'}

    return render(request, 'etablissement/add.html', context=context)


def edit(request, slug):
    lesusers = User.objects.all()
    annees = AnneeScolaire.objects.all()
    etablissement = Etablissement.objects.get(slug=slug)
    quotes = Quote.objects.select_related('etablissement', 'save_by').filter(etablissement_id=etablissement.id)
    quote = quotes.last()
        
    if request.method == 'POST':
        
        if request.POST.get('id_supprimer_quote') == 'yes':
            quote_id = request.POST.get('quote_id')
            print(quote_id)
            quote = Quote.objects.filter(slug=quote_id).delete()
            

            return redirect(f'/etablissements/')
        
        if request.POST.get('modification') == 'modifier_quote':
            annee_id = request.POST.get('anneescolaire')
            annee = AnneeScolaire.objects.get(id=annee_id)
            effectif = request.POST.get('effectif')
            versement = request.POST.get('versement')
            paid = request.POST.get('paid')
            is_ok = request.POST.get('is_ok')
            comments = request.POST.get('comments')
            if effectif is not None:
                quote.annee_scolaire = annee
                quote.effectif = effectif
                quote.versement =versement
                quote.paid = paid
                quote.is_ok = is_ok
                quote.comments = comments
                quote.save()
                messages.success(request,  f"Les données 'Quote part {etablissement.name}' ont été mises à jour avec succès.") 
                return redirect(f'/etablissements/')
            
        if request.POST.get('ajouter_quote') == 'ajouter_quote':
            annee_scolaire_new = request.POST.get('annee_scolaire_new')
            effectif_new = request.POST.get('effectif_new')
            versement_new = request.POST.get('versement_new')
            paid_new = request.POST.get('paid_new')
            is_ok_new = request.POST.get('is_ok_new')
            comments_new = request.POST.get('comments_new')
            save_by_id = request.user.id
            print(request.POST)
            if effectif_new:
                Quote.objects.update_or_create(
                annee_scolaire = annee_scolaire_new,
                effectif = effectif_new,
                versement =versement_new,
                paid = paid_new,
                is_ok = is_ok_new,
                comments = comments_new,
                save_by_id=save_by_id,
                etablissement_id =etablissement.id,
                )
                messages.success(request,  f"Les nouvelles données 'Quote part {etablissement.name}' ont été ajoutées avec succès.") 
                return redirect(f'/colleges/')
            
        if request.POST.get('modification') == 'modifier_college':
            name = request.POST.get('name')
            type_etablissement = request.POST.get('type_etablissement')
            address = request.POST.get('address')
            nomce = request.POST.get('nomce')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            if etablissement:
                etablissement.name = name
                etablissement.type_etablissement = type_etablissement
                etablissement.address = address
                etablissement.nomce = nomce
                etablissement.email = email
                etablissement.phone = phone
                etablissement.save()
                messages.success(request,   f"Les données de '{etablissement.name}' ont été mises à jour avec succès.") 
                return redirect(f'/etablissements/{slug}/')

    return render(request, 'etablissement/edit.html', {
        'etablissement': etablissement,
        'users': lesusers,
        'quote': quotes.last(),
        'lesquotes': quotes,
        "annees": annees,
    })


def delete(request, slug):
    etablissement = Etablissement.objects.get(slug=slug)
    etablissement.delete()

    return redirect(f'/etablissements/')



def delete_quote(request, slug, quote_id):
    etablissement = Etablissement.objects.get(slug=slug)
    quote = etablissement.quoteparts.get(slug=quote_id)
    print(quote)
    # quote.delete()

    return redirect(f'/etablissements/')

