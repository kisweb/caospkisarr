import re
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django_extensions.db.fields import AutoSlugField
from django.db.models import F
from helpers.util import h_random_ascii, slugify
import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

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
        return annee.pk
