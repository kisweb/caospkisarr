from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

 
# Register your models here.

from .models import User
        
class AdminAcount(ImportExportModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_superuser')
    
admin.site.register(User, AdminAcount)