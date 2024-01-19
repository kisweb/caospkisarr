from django.db import models
from account.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import uuid

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Role(models.Model):

    #__Roles_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Roles_FIELDS__END
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name        = _("Role")
        verbose_name_plural = _("Roles")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

