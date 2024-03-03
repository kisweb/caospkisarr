from django import forms
from account.models import User

class FilterUserForm(forms.ModelForm):
    email = forms.ModelChoiceField(
        queryset=User.objects.all(),
    )
    class Meta:
        model = User
        fields = ('id', 'email')
    
  