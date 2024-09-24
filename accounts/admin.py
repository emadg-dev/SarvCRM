from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserAddForm, UserChangeForm

class CustomUserAdmin(UserAdmin): 
    add_form = UserAddForm 
    form = UserChangeForm 
    model = CustomUser
    
    

    
admin.site.register(CustomUser, CustomUserAdmin)
