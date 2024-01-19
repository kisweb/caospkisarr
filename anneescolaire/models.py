import uuid
from django.db import models

# Create your models here.

import datetime
from django.db import models

class AnneeScolaire(models.Model):
    class AnneeScolaires(models.TextChoices):
        ANNEE_2023_2024 = '2023-2024', '2023-2024'
        ANNEE_2024_2025 = '2024-2025', '2024-2025'
        ANNEE_2025_2026 = '2025-2026', '2025-2026'
        ANNEE_2026_2027 = '2026-2027', '2026-2027'
        ANNEE_2027_2028 = '2027-2028', '2027-2028'
        ANNEE_2028_2029 = '2028-2029', '2028-2029'
        ANNEE_2029_2030 = '2029-2030', '2029-2030'
    
    annee = models.CharField(max_length=9, choices=AnneeScolaires.choices, unique=True)
    active = models.BooleanField(default=True)
    statut = models.CharField(max_length=20, blank=True, default="anneeEnCours")
    
    class Meta: 
        verbose_name = "anneeScolaire"
        verbose_name_plural = "anneeScolaires"

    def __str__(self):
        return self.annee
    
    @property
    def get_annee_en_cours(self, **kwargs):
        annee = self.objects.get(statut='anneeEnCours')
        return annee
    
    
        

