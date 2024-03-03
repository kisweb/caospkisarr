from account.models import User
from etablissement.models import Etablissement
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate users from Etablissement'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--superuser', action='store_true', help='Create a superuser account')

    def handle(self, *args, **kwargs):
        superuser = kwargs['superuser']
        
        username = "caosp6"
        email = "caosp6@gmail.com"
        password = "caosp"

        if superuser:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {user.username} with id {user.id} added successfully!'))
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {user.username} with id {user.id} added successfully!'))
