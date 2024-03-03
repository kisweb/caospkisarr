import django_filters
from account.models import User

class UserFilterSet(django_filters.FilterSet):
    
    class Meta:
        model = User
        fields = ('email',)