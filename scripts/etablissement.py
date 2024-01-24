
from django.db import connection


from etablissement.models import Etablissement, Ief


def run():
    # email = 'cem-ahoune-sane@caosp.zig'
    # mail = email.split('@')[0]
    # # email = mail+'@caosp.zig'
    # print(mail)
    etablissement = Etablissement.objects.first()
    print(etablissement)
    print(connection.queries)