from django.db import models
from auditlog.registry import auditlog
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser   
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
    
    # def GetCost(self):
    #     return self.product.product.price

class Status(models.Model):

    name = models.CharField(max_length=30, default='')  
    #last_name = models.CharField(max_length=30, default='')  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Procedure(models.Model):
    
    user = models.ForeignKey(CustomUser,
            on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,
            on_delete=models.PROTECT)
    status = models.ForeignKey(Status,
            on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



auditlog.register(Customer)
auditlog.register(Procedure)