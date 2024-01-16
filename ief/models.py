import uuid

from django.db import models

from account.models import User


class Ief(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    academie = models.CharField(max_length=255, blank=True, null=True, default="Ziguinchor")
    

    def __str__(self):
        return self.name