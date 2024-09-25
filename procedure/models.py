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

class Procedure(models.Model):
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9_.]+$', 
        message="نام کاربری تنها می‌تواند شامل حروف انگلیسی، اعداد، _ و نقطه باشد."
    )
    
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_regex],
        error_messages={
            'unique': "نام کاربری تکراری است.",
        }
    )

    persian_regex = RegexValidator(
        regex=r'^[\u0600-\u06FF\s]+$',  
        message="این فیلد را به فارسی وارد کنید."
        )
    first_name = models.CharField(max_length=30, validators=[persian_regex], default='')  
    last_name = models.CharField(max_length=30, validators=[persian_regex], default='')  

    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',  
        message="شماره تلفن را به درستی وارد کنید."
        )
    phone = models.CharField(max_length=11, validators=[phone_regex], default='')  


class Status(models.Model):

    name = models.CharField(max_length=30, default='')  
    #last_name = models.CharField(max_length=30, default='')  



auditlog.register(Customer)
auditlog.register(Procedure)