from django.db import models

from datetime import datetime
from enum import unique
from account.models import User
from django_extensions.db.fields import AutoSlugField
from helpers.util import h_random_ascii
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from etablissement.models import Tresorerie


class Personne(models.Model):
    
    JUSTIFICATION_TYPES = (
        ('CNI', 'Numéro CNI'),
        ('NINEA', 'NINEA'),
    )
    
    PERSONNE_TYPES = (
        ('FOURNISSEUR', 'Fournisseur'),
        ('BENEFICIAIRE', 'Bénéficiaire'),
    )
    
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, null=True)
    piece = models.CharField(max_length=10, choices=JUSTIFICATION_TYPES, null=True)
    personne_type = models.CharField(max_length=20, choices=PERSONNE_TYPES, null=True)
    numero = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    service = models.CharField(max_length=120, null=True, blank=True)
    locality = models.CharField(max_length=70, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = "personne"
        verbose_name_plural = "personnes"

    def __str__(self):
        return self.name     


class Commande(models.Model):
    fournisseur = models.ForeignKey(Personne, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True) 
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.PositiveIntegerField(default=0, null=True, blank=True)
    sorties = GenericRelation("Depense", related_query_name="commande")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.transaction_id)  


class CommandeArticle(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, related_name="articles", blank=True, null=True)
    designation = models.CharField(max_length=200)
    reference = models.CharField(max_length=200, blank=True, null=True)
    quantite = models.PositiveIntegerField(default=0, null=True, blank=True)
    prix = models.PositiveIntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        total = self.quantite * self.prix
        return total

  
class Facture(models.Model):

    FACTURE_TYPE = [
        ('R', 'RECU'),
        ('P', 'FACTURE PROFORMA'),
        ('F', 'FACTURE')
    ]
    commande = models.ForeignKey('Commande', related_name="commande", on_delete=models.SET_NULL, null=True)
    beneficiaire = models.ForeignKey(Personne, related_name="factures", on_delete=models.SET_NULL, null=True)
    tva = models.PositiveIntegerField(default=10)
    remise = models.PositiveIntegerField(default=0)
    expedition = models.PositiveIntegerField(default=0)
    paid  = models.BooleanField(default=False)
    facture_type = models.CharField(max_length=1, choices=FACTURE_TYPE)   
    reference = models.CharField(max_length=120, default=h_random_ascii(8))
    comments = models.TextField(null=True, max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
           return f"{self.created}_{self.get_total}"

    @property
    def get_total(self):
        articles = self.commande.articles.all()   
        total = sum(article.get_total for article in articles)
        return total
    
    @property
    def get_tva(self):
        latva = self.get_total * self.tva/100
        return int(latva)
    
    @property
    def get_remise(self):
        la_remise = self.get_total * self.remise/100
        return int(la_remise)
    
    @property
    def get_montant_net(self):
        montant = self.get_total * (1 + self.tva/100) + self.expedition - self.get_remise
        return int(montant)


class Depense(models.Model):
    class TypeMouvement(models.TextChoices):
        SORTIE = 'Sortie', 'Sortie'
        REGULARISATION = 'Regularisation', 'Régularisation'
        ATTENTE = 'Attente', 'Attente'
        
    mouvement = models.CharField(max_length=20, choices=TypeMouvement.choices, null=True, default='Sortie')
    montant = models.PositiveIntegerField(default=0, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=0, null=True)
    content_objet = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f"{self.mouvement} {self.montant}"
    
    class Meta:
        indexes = [ 
            models.Index(fields=['content_type', 'object_id']),   
        ]


def get_depense_general():
    factures = Facture.objects.all()
    
    depense_general = sum(facture.get_montant_net for facture in factures)
    return depense_general
