from django.shortcuts import render, reverse, redirect
from django.contrib import messages
import datetime
from .models import Category, Beneficiaire, Order, Article, Facture
from .forms import CategoryCreateForm, BeneficiaireCreateForm, OrderCreateForm, ArticleCreateForm, FactureCreateForm

def index(request):
    
    context = {
        'segment': 'commande-index', 
        'categories': Category.objects.all(),
        'beneficiaires': Beneficiaire.objects.all(),
        'commandes': Order.objects.all(),
        'factures': Facture.objects.all(),
    }

    return render(request, 'commande/index.html', context=context)

def category(request):
    categories = Category.objects.all()
    form = CategoryCreateForm()
    
    context = {'segment': 'commande-cat', 'form': form, 'categories': categories }

    return render(request, 'commande/category.html', context=context)

def order(request):
    orders = Order.objects.all()
    form = OrderCreateForm()
    if request.method == 'POST':  
        order_object = {
            'name': request.POST.get('name'),
            'code': request.POST.get('code'),
            'order_type': request.POST.get('order_type'),
            'valided_on': request.POST.get('valided_on')        
        }      
        print(request.POST)
        order = Order.objects.create(**order_object)
        if order:
            messages.success(request,  f"Les données '{order.name}' ont été ajoutées avec succès.")
            return redirect(f'commande:order')
     
    context = {'segment': 'commande-order', 'form': form, 'orders': orders }

    return render(request, 'commande/order.html', context=context)

def article(request):
    articles = Article.objects.all()
    form = ArticleCreateForm()
    
    context = {'segment': 'commande-article', 'form': form, 'articles': articles }

    return render(request, 'commande/article.html', context=context)

def beneficiaire(request):
    
    beneficiaires = Beneficiaire.objects.all()
    form = BeneficiaireCreateForm()
    if request.method == 'POST':  
        benef_object = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'piece': request.POST.get('piece'),
            'numero': request.POST.get('numero'),
            'address': request.POST.get('address'),
            'service': request.POST.get('service'),
            'locality': request.POST.get('locality')            
        }      
        
        print(request.POST)
        benef = Beneficiaire.objects.create(**benef_object)
        if benef:
            messages.success(request,  f"Les données '{benef.name}' ont été ajoutées avec succès.")
            return redirect(f'/commandes/beneficiaires/')
        
    context = {'segment': 'commande-benef', 'form': form, 'beneficiaires': beneficiaires }

    return render(request, 'commande/beneficiaire.html', context=context)

def facture_add(request):
    factures = Facture.objects.all()
    form = FactureCreateForm()
    context = {'segment': 'commande-facture', 'form': form, 'factures': factures, 'beneficiaires': Beneficiaire.objects.all() }

    return render(request, 'commande/add-facture.html', context=context)

def facture_print(request, pk):
    facture = Facture.objects.filter(id=pk).select_related('order', 'beneficiaire')
    
    context = {'segment': 'commande-facture-print', 'facture': facture, 'beneficiaires': Beneficiaire.objects.all() }

    return render(request, 'commande/facture.html', context=context)
