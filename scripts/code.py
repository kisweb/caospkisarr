from core.models import Profile
from etablissement.models import Etablissement, Quote
from helpers import h_random_ascii, generate_username, validate_fullname

def run():
    # code = ""
    # for i in range(1,200):
    #     code = h_random_ascii(8)
    # #return code
    
    #     print(code)
    # obj = Etablissement.objects.filter(ief='Oussouye', type_etablissement='Lycée').all()

    # # etablissements = obj.quote_set__versement

    # context = {
    #     'obj': obj,
    # }

    # print(obj)
    
    user = Profile.objects.get(pk=1)
    print(user)
    first_name = user.first_name
    last_name = user.last_name
    name = user.first_name+" "+user.last_name
    pseudo = generate_username(self=user, full_name='MODOU OUMAR DIOUF', Model=Profile)
    validate_fullname(name)
    print(pseudo+'@caosp.zig')
    
    print(validate_fullname('MODOU ISSA DIOP'))