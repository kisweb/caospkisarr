
from django.db import connection
from pprint import pprint

from etablissement.models import Etablissement, Ief


def run():
    # email = 'cem-ahoune-sane@caosp.zig'
    # mail = email.split('@')[0]
    # # email = mail+'@caosp.zig'
    # print(mail)
    etablissements = Etablissement.objects.all()
    pprint(etablissements.first().__dict__)
    pprint(connection.queries)
    
    