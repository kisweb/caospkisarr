from core.models import Profile
from etablissement.models import Etablissement, Quote
# from helpers import h_random_ascii, generate_username, validate_fullname

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_fullname(self):
    fullname = self.split()
    if len(fullname) <= 1:
        raise ValidationError(
            _('Kindly enter more than one name, please.'),
            code='invalid',
            params={'value': self},
        )
    for x in fullname:
        if x.isalpha() is False or len(x) < 2:
            raise ValidationError(
                _('Please enter your name correctly.'),
                code='invalid',
                params={'value': self},
            )


def get_first_name(self):
    fullname = self.split()
    long = len(fullname)
    if long > 2:
        names = fullname[0:long-1]
        
    else:
        names = fullname[0]
    
    return names


def get_last_name(self):
    if isinstance(self, bool):
        pass
    else:
        names = self.split()
        return names[-1]


def generate_username(self, full_name, Model):
    name = full_name.lower()
    name = name.split(' ')
    lastname = name[-1]
    firstname = get_first_name(full_name)
    # prenom = firstname.split()
    self.username = '%s%s' % (firstname, lastname)
    if Model.objects.filter(username=self.username).count() > 0:
        username = '%s%s' % (firstname, lastname[0])
        if Model.objects.filter(username=self.username).count() > 0:
            users = Model.objects.filter(username__regex=r'^%s[1-9]{1,}$' % firstname).order_by(
                'username').values(
                'username')
            if len(users) > 0:
                last_number_used = sorted(
                    map(lambda x: int(x['username'].replace(firstname, '')), users))
                last_number_used = last_number_used[-1]
                number = last_number_used + 1
                self.username = '%s%s' % (firstname, number)
            else:
                self.username = '%s%s' % (firstname, 1)
    return self.username



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
    pseudo = generate_username(self=user, full_name=('MODOU OUMAR DIOUF'), Model=Profile)
    validate_fullname(name)
    print(pseudo+'@caosp.zig')
    print(get_first_name('el hadji MODOU ISSA DIOP'))
    