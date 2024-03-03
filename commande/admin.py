from django.contrib import admin
# from django.contrib.contenttypes.admin import TabularInline

from account.models import User

from .models import Category, Order, Article, Beneficiaire, Facture

class ArticleInline(admin.TabularInline):
    model = Article
    max_num = 10
    
    
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', )
    
class AdminBeneficiaire(admin.ModelAdmin):
    list_display = ('name','service', 'numero', 'phone' )
    
class AdminOrder(admin.ModelAdmin):
    list_display = ('order_type', 'name', 'code')
    
    
class AdminArticle(admin.ModelAdmin):
    list_display = ['category', 'facture', 'name','quantity', 'unit_price', 'get_total']
    
    
class AdminFacture(admin.ModelAdmin):
    list_display = ('order', 'beneficiaire', 'get_total')
    inlines = [ArticleInline]
 
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)
admin.site.register(Article, AdminArticle)
admin.site.register(Beneficiaire, AdminBeneficiaire)
admin.site.register(Facture, AdminFacture)
