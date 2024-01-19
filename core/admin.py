from django.contrib import admin

# Register your models here.

from .models import Profile, Role
from account.models import User
      
class AdminRole(admin.ModelAdmin):
    list_display = ('name',)    
      
class AdminProfile(admin.ModelAdmin):
    list_display = (Profile.user.field.name, 'role',)
    
admin.site.register(Role, AdminRole)
admin.site.register(Profile, AdminProfile)