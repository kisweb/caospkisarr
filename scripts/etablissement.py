


from etablissement.models import Etablissement


def run():
    email = 'cem-ahoune-sane@caosp.zig'
    mail = email.split('@')[0]
    # email = mail+'@caosp.zig'
    print(mail)
    etablissement = Etablissement.objects.get(slug=mail)
    print(etablissement)