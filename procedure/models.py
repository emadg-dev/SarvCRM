from django.db import models
from auditlog.registry import auditlog
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser 
import jdatetime
 
# import django_jalali.db.models as jmodels
 
from django.core.validators import RegexValidator

    
class Customer(models.Model):
    user = models.ForeignKey(CustomUser,
            on_delete=models.PROTECT)
    # product = models.ForeignKey(Stock, 
            # on_delete=models.CASCADE)
    #quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    
    owner = models.CharField(max_length=50, )
    SSN = models.CharField(max_length=10, default='', blank=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=11)
    lock = models.CharField(max_length=6, default='', blank=True)

    open = 'مذاکره'
    deadend = 'بن بست'
    Status_Options = [(open, 'مذاکره'),
        (deadend, 'بن بست'),]
    status = models.CharField(max_length=50, choices=Status_Options, default=open)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dispach = 'دیسپچ سرو'
    sepidz = 'دیسپچ سپیدز'
    customers = 'مشتریان'
    internet = 'اینترنت'
    website = 'وبسایت'
    refferal = 'راه‌انداز'
    Lead_Options = [(dispach, 'دیسپچ سرو'),
        (sepidz, 'دیسپچ سپیدز'), (customers, 'مشتریان'),
        (internet, 'اینترنت'), (website, 'وبسایت'),
        (refferal, 'راه‌انداز'),
        ]
    lead = models.CharField(max_length=50, choices=Lead_Options, default=open)                 
  
    def get_absolute_url(self): 
        return reverse('dashboard')
    
    def __str__(self):
        return str (self.name + " - " + self.branch + " : " + self.owner)
    
    def get_jalali_created_at(self):
        # Convert Gregorian date to Jalali
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d %H:%M:%S')

    def get_jalali_updated_at(self):
        # Convert Gregorian date to Jalali
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y/%m/%d %H:%M:%S')
    
    # def GetCost(self):
    #     return self.product.product.price

class Status(models.Model):

    name = models.CharField(max_length=30, default='')  
    #last_name = models.CharField(max_length=30, default='')  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str (self.name)

class Procedure(models.Model):
    
    user = models.ForeignKey(CustomUser,
            on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,
            on_delete=models.PROTECT)
    status = models.ForeignKey(Status,
            on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, default='', blank=True) 

    def __str__(self):
        return str (self.customer + " - " + self.user) 



auditlog.register(Customer)
auditlog.register(Procedure)