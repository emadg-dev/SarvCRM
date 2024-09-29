from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from accounts.models import CustomUser


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'is_staff', 
            'phone', 
            'is_active', 
            'email', 
        ]
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'is_staff': 'مدیر',
            'phone': 'شماره تلفن',
            'is_active': 'فعال',
            'email': 'ایمیل',
        }
    