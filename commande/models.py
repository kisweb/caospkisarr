from django.db import models
from datetime import datetime
from enum import unique
from account.models import User
from django_extensions.db.fields import AutoSlugField
from helpers.util import h_random_ascii



class Beneficiaire(models.Model):
    
    JUSTIFICATION_TYPES = (
        ('CNI', 'Numéro CNI'),
        ('NINEA', 'NINEA'),
    )
     
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, null=True)
    piece = models.CharField(max_length=10, choices=JUSTIFICATION_TYPES, null=True)
    numero = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    service = models.CharField(max_length=120, null=True, blank=True)
    locality = models.CharField(max_length=70, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = "beneficiaire"
        verbose_name_plural = "beneficiaires"

    def __str__(self):
        return self.name     


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="name")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "categorie"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
 
 
class Article(models.Model):
    class TypeArticle(models.TextChoices):
        UNITE = "1", "Unité"
        LITRE = "2", "Litre"
        KILO = "3", "Kilogramme"
        CARTON = "4", "Carton"
        CAISSE = "5", "Caisse"
        VRAC = "6", "En vrac"
        
    category = models.ForeignKey("Category", related_name="articles", on_delete=models.SET_NULL, null=True)
    facture = models.ForeignKey("Facture", related_name="articles", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=50, blank=True, null=True)
    unity = models.CharField(
        max_length=1, choices=TypeArticle.choices, null=True, default='1'
    )
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        
    def __str__(self):
           return f"{self.name}_{self.get_total}"

    @property
    def get_total(self):
        total = self.quantity * self.unit_price   
        return total
    
   
class Facture(models.Model):

    FACTURE_TYPE = [
        ('R', 'RECU'),
        ('P', 'FACTURE PROFORMA'),
        ('F', 'FACTURE')
    ]
    order = models.ForeignKey('Order', related_name="order", on_delete=models.SET_NULL, null=True)
    facture_date_time = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)
    tva = models.PositiveIntegerField(default=10)
    remise = models.PositiveIntegerField(default=0)
    expedition = models.PositiveIntegerField(default=0)
    last_updated_date = models.DateTimeField(null=True, blank=True)
    paid  = models.BooleanField(default=False)
    facture_type = models.CharField(max_length=1, choices=FACTURE_TYPE)    
    reference = models.CharField(max_length=120, null=True, blank=True)
    comments = models.TextField(null=True, max_length=1000, blank=True)
    beneficiaire = models.ForeignKey(Beneficiaire, related_name="factures", on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
           return f"{self.facture_date_time}_{self.get_total}"

    @property
    def get_total(self):
        articles = self.articles.all()   
        total = sum(article.get_total for article in articles)
        return total
    
    def get_tva(self):
        return self.get_total() * self.tva/100
    
    def get_montant_net(self):
        montant = self.total * (1 + self.tva/100) + self.expedition - self.remise
        return montant


class Order(models.Model):
    
    class TypeOrder(models.TextChoices):
        PRODUIT = "Produit", "Produit"
        BIEN = "Bien", "Bien"
        SERVICE = "Service_Prestation", "Service et prestation"
        AUTRE = "autre", "Autre"
       
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=32, default=h_random_ascii(10))
    order_type = models.CharField(
        max_length=20, choices=TypeOrder.choices, null=True, default='autre'
    )
    fournisseur = models.ForeignKey('Beneficiaire', related_name='fournisseur', on_delete=models.SET_NULL, null=True)
    valided_on = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return self.name
 