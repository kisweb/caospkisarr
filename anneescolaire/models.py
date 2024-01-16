from django.db import models

# Create your models here.

import datetime
from django.db import models

class AnneeScolaire(models.Model):
    
    annee = models.CharField(max_length=9, unique=True, db_index=True)
    active = models.BooleanField(default=True)
    statut = models.CharField(max_length=20, blank=True, default="anneeEnCours")
    
    class Meta: 
        verbose_name = "anneeScolaire"
        verbose_name_plural = "anneeScolaires"

    def __str__(self):
        return self.annee
        
