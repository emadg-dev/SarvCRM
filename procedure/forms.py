from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Customer

class CustomeraddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'lock', 
            'name', 
            'branch', 
            'owner', 
            'SSN', 
            'phone', 
            'address', 
            'status', 
            'lead'
        ]
        labels = {
            'lock': 'قفل',
            'name': 'نام',
            'branch': 'شعبه',
            'owner': 'مالک',
            'SSN': 'شماره ملی',
            'phone': 'تلفن',
            'address': 'آدرس',
            'status': 'وضعیت',
            'lead': 'منبع',
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomeraddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'row g-3'  # Bootstrap 5 class for row spacing
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('branch', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('SSN', css_class='col-md-6'),
                Column('owner', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('address', css_class='col-md-6'),
                Column('phone', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('lock', css_class='col-md-6'),
                Column('status', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('lead', css_class='col-md-6'),
                css_class='row'
            ),
            Submit('submit', 'ثبت', css_class='btn btn-primary')
        )

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'lock', 
            'name', 
            'branch', 
            'owner', 
            'SSN', 
            'phone', 
            'address', 
            'status', 
            'lead'
        ]
        labels = {
            'lock': 'قفل',
            'name': 'نام',
            'branch': 'شعبه',
            'owner': 'مالک',
            'SSN': 'شماره ملی',
            'phone': 'تلفن',
            'address': 'آدرس',
            'status': 'وضعیت',
            'lead': 'منبع',
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'row g-3' 
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('branch', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('SSN', css_class='col-md-6'),
                Column('owner', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('address', css_class='col-md-6'),
                Column('phone', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('lock', css_class='col-md-6'),
                Column('status', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('lead', css_class='col-md-6'),
                css_class='row'
            ),
            Submit('submit', 'ثبت', css_class='btn btn-primary')
        )
