import re
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django_extensions.db.fields import AutoSlugField
from django.db.models import F
from account.models import User
from caosp.settings import ANNEES
from anneescolaire.models import AnneeScolaire
from helpers.util import h_random_ascii
from caosp.utils import slugify
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

class Ief(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug: str = AutoSlugField(populate_from="name")
    description = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "ief"
        verbose_name_plural = "iefs"

    def __str__(self):
        return self.slug
    
    
class Etablissement(models.Model):
    """
    Name: Etablissement model definition
    """

    class IEF(models.TextChoices):
        BIGNONA1 = "Bignona1", "Bignona 1"
        BIGNONA2 = "Bignona2", "Bignona 2"
        OUSSOUYE = "Oussouye", "Oussouye"
        ZIGUINCHOR = "Ziguinchor", "Ziguinchor"

    class TypeEtablissement(models.TextChoices):
        COLLEGE = "College", "Collège"
        LYCEE = "Lycee", "Lycée"
        MIXTE = "mixte", "Lycée Mixte"
        AUTRE = "autre", "Autre"

    name = models.CharField(max_length=132)
    slug: str = AutoSlugField(populate_from="name")
    code = models.CharField(max_length=16)
    ief = models.ForeignKey(Ief, related_name="etablissements", on_delete=models.SET_NULL, null=True)
    type_etablissement = models.CharField(
        max_length=20, choices=TypeEtablissement.choices, null=True, default='autre'
    )
    nomce = models.CharField(max_length=132, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, related_name="etablissements", on_delete=models.SET_NULL, null=True)
    versements = GenericRelation("Tresorerie", related_query_name="etablissent")

    class Meta:
        verbose_name = "Etablissement"
        verbose_name_plural = "Etablissements"

    def __str__(self):
        return self.slug

    @property
    def nbEtabsIef(self, id:int=None, **kwargs):
        etabs = self.objects.filter(ief_id=id).all()
        return etabs.count()    


class Quote(models.Model):
    class QuoteAnneeScolaires(models.TextChoices):
        ALL = "ALL"
        ANNEE_2023_2024 = "2023-2024" , "2023-2024"
        ANNEE_2024_2025 = "2024-2025" , "2024-2025"
        ANNEE_2025_2026 = "2025-2026" , "2025-2026"
        ANNEE_2026_2027 = "2026-2027" , "2026-2027"
        ANNEE_2027_2028 = "2027-2028" , "2027-2028"
        ANNEE_2028_2029 = "2028-2029" , "2028-2029"
        ANNEE_2029_2030 = "2029-2030" , "2029-2030"


    etablissement = models.ForeignKey(
        Etablissement, related_name="quotes", on_delete=models.CASCADE, null=True
    )
    annee_scolaire = models.ForeignKey(
        AnneeScolaire, related_name="quotes", on_delete=models.CASCADE
    )
    save_by = models.ForeignKey(User, related_name="quotes", null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=130)
    effectif = models.IntegerField(null=False, blank=False, default=0)
    versement = models.IntegerField(null=False, blank=False, default=0)
    quote_date_time = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    paid = models.BooleanField(default=False)
    is_ok = models.BooleanField(default=False)
    comments = models.TextField(null=True, max_length=1000, blank=True)

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return f"{self.etablissement.slug}_{self.annee_scolaire.annee}"
    
    def get_slug(self):
         return '%s-%s' % (slugify(self.etablissement), slugify(self.annee_scolaire.annee))

    def check_slug(self, slug):
        # ensure uniqueness
        while(Quote.objects.filter(slug__iexact=slug).count()):  # if not unique
            suff = re.search("\d+$", slug)  # get the current number suffix if present
            suff = suff and suff.group() or 0
            next = str(int(suff) +1)  # increment it & turn to string for re.sub
            slug = re.sub("(\d+)?$", next, slug)  # replace with higher suffix, retry
        return slug

    def save(self, *args, **kwargs):
        #...
        slug = self.get_slug()
        if not self.pk or (self.pk and not slug in self.slug):
            self.slug = self.check_slug(slug)
        super(Quote, self).save(*args, **kwargs)
        
        
    @property
    def get_montant(self):
        montant = self.effectif * 100
        return montant


class Tresorerie(models.Model):
    class TypeMouvement(models.TextChoices):
        ENTREE = 'Entree', 'Entrée'
        SORTIE = 'Sortie', 'Sortie'
        REGULARISATION = 'Regularisation', 'Régularisation'
        ATTENTE = 'Attente', 'Attente'
        
    mouvement = models.CharField(max_length=20, choices=TypeMouvement.choices, null=True, default='Entree')
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


def get_montant_general(annee = None):
    quotes = Quote.objects.all()
    if annee is not None:
        quotes = Quote.objects.filter(annee_scolaire=annee).all()
        
    montant_general = sum(quote.versement for quote in quotes)
    return montant_general


@receiver(post_save, sender=Etablissement)
def create_quote_etablissement(sender, instance, created, **kwargs):
    if created:
        Quote.objects.create(
            etablissement=instance,
            annee_scolaire=AnneeScolaire.objects.filter(statut='anneeEnCours').first(),
            save_by=User.objects.filter(is_staff=True).first()
        )


# @receiver(post_save, sender=Etablissement)
# def save_quote_etablissement(sender, instance, **kwargs):
#     instance.quote.save()
    

