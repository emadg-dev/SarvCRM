from django import forms 
from accounts import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class UserAddForm(UserCreationForm):
    class Meta(UserCreationForm): 
        model = models.CustomUser 
       
        fields = UserCreationForm.Meta.fields + ('first_name' , 'last_name', 'phone', 'is_staff')
        
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone': 'شماره تلفن',
            'is_staff': 'دسترسی',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-field'}),
            'last_name': forms.TextInput(attrs={'class': 'form-field'}),
            'phone': forms.TextInput(attrs={'class': 'form-field'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-field'}),
        }

# class UserChangeForm(UserChangeForm):
#     class Meta: 
#         model = models.CustomUser 
#         fields = UserChangeForm.Meta.fields