from django import forms
from anneescolaire.models import AnneeScolaire

from commande.models import Beneficiaire, Order, Category, Article, Facture


class OrderCreateForm(forms.ModelForm): 
    valided_on = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control", "type":"date"}))   
    class Meta:
        model = Order
        fields = ('name', 'code', 'order_type', 'valided_on', 'fournisseur')
        

class FactureCreateForm(forms.ModelForm):    
    class Meta:
        model = Facture
        fields = ('order', 'beneficiaire', 'remise', 'tva', 'expedition', 'paid', 'facture_type', 'reference', 'comments')
        
class ArticleCreateForm(forms.ModelForm):    
    class Meta:
        model = Article
        fields = ('category', 'facture', 'name', 'reference', 'unity', 'quantity', 'unit_price')
        
class BeneficiaireCreateForm(forms.ModelForm):    
    class Meta:
        model = Beneficiaire
        fields = ('name', 'piece', 'numero', 'service', 'address', 'phone', 'locality')
        
        
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
