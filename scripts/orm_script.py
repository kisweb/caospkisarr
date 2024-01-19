from account.models import User
from anneescolaire.models import AnneeScolaire
from etablissement.models import Etablissement, Quote, get_montant_general
from django.utils import timezone
 
def run():
    # etablissement = Etablissement()
    # etablissement.name ="CEM Malick Fall"
    # etablissement.slug = "cem-malick-fall"
    # etablissement.code = "M@l1cK"
    # etablissement.ief  = "Bignona1"
    # etablissement.type_etablissement = "college"
    # etablissement.nomce = "Sambou Ndour"
    # etablissement.email = "malick@caosp.zig"
    # etablissement.phone = "339911346"
    # etablissement.address = "Ziguinchor"
    # etablissement.created_date = timezone.now
    # etablissement.save_by = User.objects.first()
    # etablissement.save()
    
    # print(etablissement)
    
    # etablissement=Etablissement.objects.first()
    
    print(get_montant_general())