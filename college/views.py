import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from quote.decorators import superuser_required
from login_required import login_not_required
from .models import College, Quote
from account.models import User
from ief.models import Ief
from caosp.settings import ANNEES
from helpers.util import *
from college.forms import FilterQuoteAnneeForm

from caosp.utils import unique_slug_generator


def colleges(request):
    iefs = Ief.objects.all()
    colleges = College.objects.select_related('quote', 'conseiller', 'added_by').all()
    return render(request, 'college/colleges.html', {
        'colleges': colleges,
        'iefs': iefs,
        'segment': 'college-list'

    })


def college(request, slug):
    # quotes = Quote.select_related('college', 'save_by').get(college=pk)
    college = College.objects.select_related('conseiller', 'added_by').get(slug=slug)
    form = FilterQuoteAnneeForm()
    print(college)
    if request.POST.get('id_supprimer') == "yes":
        college.delete()
        messages.success(request,  f"Toutes les données de '{college.etablissement}' ont été supprimées.") 
        return redirect(f'/colleges/')
        
    return render(request, 'college/college.html', {
        'college': college,
        'annees': ANNEES
    })


def add(request):
    les_iefs = Ief.objects.all()
    lesusers = User.objects.all()
    print(lesusers)
    if request.method == 'POST':
        
        code = h_random_ascii(8)
        etablissement = request.POST.get('etablissement')
        slug = unique_slug_generator(request.POST.get('etablissement'))
        statut = request.POST.get('statut')
        adresse = request.POST.get('adresse')
        ief_id = request.POST.get('ief')
        nomce = request.POST.get('nomce')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        fixe = request.POST.get('fixe')
        conseiller_id = request.POST.get('conseiller')
        
        print(request.POST)
        if etablissement:
            College.objects.create(
                code=h_random_ascii(8), 
                etablissement=etablissement,
                slug=slug,
                email=email, 
                ief_id=ief_id,
                statut=statut,
                adresse=adresse,
                nomce=nomce, 
                mobile=mobile, 
                fixe=fixe ,
                conseiller_id=conseiller_id,
                added_by=request.user
            )
    context = {'segment': 'college-add', 'iefs': les_iefs, 'users': lesusers}

    return render(request, 'college/add.html', context=context)


def edit(request, slug):
    lesiefs = Ief.objects.all()
    lesusers = User.objects.all()
    college = College.objects.get(slug=slug)
    quotes = Quote.objects.select_related('college', 'save_by').filter(college_id=college.id)
    quote = quotes.last()
        
    if request.method == 'POST':
        
        if request.POST.get('modification') == 'modifier_quote':
            annee_scolaire = request.POST.get('annee_scolaire')
            effectif = request.POST.get('effectif')
            versement = request.POST.get('versement')
            montant = quote.get_montant
            paid = request.POST.get('paid')
            is_ok = request.POST.get('is_ok')
            comments = request.POST.get('comments')
            if effectif is not None:
                quote.annee_scolaire = annee_scolaire
                quote.effectif = effectif
                quote.versement =versement
                quote.montant= montant
                quote.paid = paid
                quote.is_ok = is_ok
                quote.comments = comments
                quote.save()
                messages.success(request,  f"Les données 'Quote part {college.etablissement}' ont été mises à jour avec succès.") 
                return redirect(f'/colleges/')
            
        if request.POST.get('ajouter_quote') == 'ajouter_quote':
            annee_scolaire_new = request.POST.get('annee_scolaire_new')
            effectif_new = request.POST.get('effectif_new')
            versement_new = request.POST.get('versement_new')
            montant_new = quote.get_montant
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
                montant= montant_new,
                paid = paid_new,
                is_ok = is_ok_new,
                comments = comments_new,
                save_by_id=save_by_id,
                college_id =college.id,
                )
                messages.success(request,  f"Les nouvelles données 'Quote part {college.etablissement}' ont été ajoutées avec succès.") 
                return redirect(f'/colleges/')
            
        if request.POST.get('modification') == 'modifier_college':
            etablissement = request.POST.get('etablissement')
            statut = request.POST.get('statut')
            adresse = request.POST.get('adresse')
            nomce = request.POST.get('nomce')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            fixe = request.POST.get('fixe')
            if etablissement:
                college.etablissement = etablissement
                college.statut = statut
                college.adresse = adresse
                college.nomce = nomce
                college.email = email
                college.mobile = mobile
                college.fixe = fixe
                college.save()
                messages.success(request,   f"Les données de '{college.etablissement}' ont été mises à jour avec succès.") 
                return redirect(f'/colleges/{slug}/')

    return render(request, 'college/edit.html', {
        'college': college,
        'iefs': lesiefs,
        'users': lesusers,
        'quote': quotes.last(),
        'lesquotes': quotes,
        "annees": ANNEES
    })


def delete(request, slug):
    college = College.objects.get(slug=slug)
    college.delete()

    return redirect(f'/colleges/')

