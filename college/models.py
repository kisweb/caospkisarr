from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from account.models import User
from caosp.settings import ANNEES
from ief.models import Ief



class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=16, null=True, blank=True)
    etablissement = models.CharField(max_length=132) 
    slug: str = models.SlugField(unique=True, blank=True)
    statut = models.CharField(max_length=132, null=True, blank=True)
    nomce = models.CharField(max_length=132, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=132, null=True, blank=True)
    fixe = models.CharField(max_length=64, null=True, blank=True)
    adresse = models.CharField(max_length=250, null=True, blank=True)
    quote = models.ForeignKey('Quote', null=True, related_name='quote', on_delete=models.SET_NULL)
    conseiller = models.ForeignKey(User, related_name='conseiller', on_delete=models.PROTECT)
    ief = models.ForeignKey(Ief, related_name='ief', on_delete=models.PROTECT)
    added_by = models.ForeignKey(User, null=True, related_name='added_by', on_delete=models.SET_NULL)

    
    class Meta: 
        verbose_name = "College"
        verbose_name_plural = "Colleges"

    def __str__(self):
        return self.etablissement
    
    
class Quote(models.Model):
    class QuoteAnneeScolaires(models.TextChoices):
        ALL = "ALL"
        ANNEE_2023_2024 = '2023-2024'
        ANNEE_2024_2025 = '2024-2025'
        ANNEE_2025_2026 = '2025-2026'
        ANNEE_2026_2027 = '2026-2027'
        ANNEE_2027_2028 = '2027-2028'
        ANNEE_2028_2029 = '2028-2029'
        ANNEE_2029_2030 = '2029-2030'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    college = models.ForeignKey(College, related_name='college', on_delete=models.CASCADE)
    annee_scolaire = models.CharField(max_length=9, choices=QuoteAnneeScolaires.choices)
    effectif = models.IntegerField(null=False, blank=False, default=0)
    versement = models.IntegerField(null=False, blank=False, default=0)
    montant = models.IntegerField(null=False, blank=False, default=0)
    save_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    quote_date_time = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    paid  = models.BooleanField(default=False)
    is_ok = models.BooleanField(default=False)
    comments = models.TextField(null=True, max_length=1000, blank=True)

    
    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
           return f"{self.college.etablissement}_{self.annee_scolaire}"

    @property
    def get_montant(self):           
        montant = self.effectif * 100
        return montant 

def get_montant_general():
    quotes = Quote.objects.all()   
    montant_general = sum(quote.versement for quote in quotes)
    return montant_general           

   
def createQuote(sender, instance, created, **kwargs):
    if created:
        college = instance
        quotepart = Quote.objects.create(
            college=college,
            save_by=instance.added_by
        )
        
post_save.connect(createQuote, sender=College)
        