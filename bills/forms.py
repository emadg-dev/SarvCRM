from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import *

class BilladdForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            'number', 
            'price', 
            'customer', 
            'sub_date', 
            'due_date', 
            'factor',
            'status',  
            'comment',
        ]
        labels = {
            'number': 'شماره چک',
            'price': 'مبلغ',
            'customer': 'مشتری',
            'sub_date': 'تاریخ ثبت',
            'due_date': 'تاریخ سررسید',
            'factor': 'فاکتور',
            'status': 'وضعیت',
            'comment': 'شرح',
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(CustomeraddForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'row g-3'  # Bootstrap 5 class for row spacing
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='col-md-6'),
    #             Column('branch', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('SSN', css_class='col-md-6'),
    #             Column('owner', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('address', css_class='col-md-6'),
    #             Column('phone', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('lock', css_class='col-md-6'),
    #             Column('status', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('lead', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Submit('submit', 'ثبت', css_class='btn btn-primary')
    #     )

class BillUpdateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            'number', 
            'price', 
            'customer', 
            'sub_date', 
            'due_date', 
            'factor',
            'status',  
            'comment',
        ]
        labels = {
            'number': 'شماره چک',
            'price': 'مبلغ',
            'customer': 'مشتری',
            'sub_date': 'تاریخ ثبت',
            'due_date': 'تاریخ سررسید',
            'factor': 'فاکتور',
            'status': 'وضعیت',
            'comment': 'شرح',
        }


class FactoraddForm(forms.ModelForm):
    class Meta:
        model = Factor
        fields = [
            'number', 
            'price', 
            'customer', 
            'procedure', 
            'status',  
            'comment',
        ]
        labels = {
            'number': 'شماره ',
            'price': 'مبلغ',
            'customer': 'مشتری',
            'procedure': 'پروسه',
            'status': 'وضعیت',
            'comment': 'شرح',
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(CustomeraddForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'row g-3'  # Bootstrap 5 class for row spacing
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='col-md-6'),
    #             Column('branch', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('SSN', css_class='col-md-6'),
    #             Column('owner', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('address', css_class='col-md-6'),
    #             Column('phone', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('lock', css_class='col-md-6'),
    #             Column('status', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Row(
    #             Column('lead', css_class='col-md-6'),
    #             css_class='row'
    #         ),
    #         Submit('submit', 'ثبت', css_class='btn btn-primary')
    #     )

class FactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Factor
        fields = [
            'number', 
            'price', 
            'customer', 
            'procedure', 
            'status',  
            'comment',
        ]
        labels = {
            'number': 'شماره ',
            'price': 'مبلغ',
            'customer': 'مشتری',
            'procedure': 'پروسه',
            'status': 'وضعیت',
            'comment': 'شرح',
        }