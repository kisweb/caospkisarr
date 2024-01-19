from django.contrib import admin

# Register your models here.

from .models import User
        
class AdminAcount(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_superuser')
    
admin.site.register(User, AdminAcount)