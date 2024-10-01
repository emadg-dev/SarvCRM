from django.db import models
from auditlog.registry import auditlog
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser 
from procedure.models import Customer, Procedure 
import jdatetime


class Factor(models.Model):
    
    user = models.ForeignKey(CustomUser,
            on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,
            on_delete=models.PROTECT)
    procedure = models.ForeignKey(Procedure,
            on_delete=models.PROTECT)
    
    price = models.DecimalField(max_digits=16, decimal_places=0, blank=True)
    number = models.DecimalField(max_digits=16, decimal_places=0, blank=True)


    initial = 'اولیه'
    passed = 'تسویه شده'
    canceled = 'کنسل شده'
    Status_Options = [(initial, 'اولیه'),
        (passed, 'تسویه شده'),
        (canceled, 'کنسل شده'), 
        ]
    status = models.CharField(max_length=50, choices=Status_Options, default=initial)          

    comment = models.CharField(max_length=500, default='', blank=True) 
    created_at = models.CharField(max_length=20, editable=False)
    updated_at = models.CharField(max_length=20, editable=False)

    def get_jalali_date(self):
        current_date = jdatetime.datetime.now()
        return current_date.strftime('%Y/%m/%d')
    
    def save(self, *args, **kwargs):
        if not self.created_at:  
            self.created_at = self.get_jalali_date()
        self.updated_at = self.get_jalali_date()  
        super(Factor, self).save(*args, **kwargs)

    def __str__(self):
        return str (str(self.number) + " - " + self.customer.name + ": " + str(self.price)) 


class Bill(models.Model):
    
    user = models.ForeignKey(CustomUser,
            on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,
            on_delete=models.PROTECT)
    factor = models.ForeignKey(Factor,
            on_delete=models.PROTECT)
    
    price = models.DecimalField(max_digits=16, decimal_places=0, blank=True)
    number = models.DecimalField(max_digits=16, decimal_places=0, blank=True)
    initial = 'اولیه'
    submitted = 'ثبت شده'
    archived = 'دریافت شده'
    due = 'سر رسیده'
    failed = 'برگشت خورده'
    passed = 'پاس شده'
    Status_Options = [(initial, 'اولیه'),
        (submitted, 'ثبت شده'), (archived, 'دریافت شده'),
        (due, 'سر رسیده'), (failed, 'برگشت خورده'),
        (passed, 'پاس شده'),
        ]
    status = models.CharField(max_length=50, choices=Status_Options, default=initial)          
    sub_date = models.CharField(max_length=20, blank=True)
    due_date = models.CharField(max_length=20, blank=True)

    comment = models.CharField(max_length=500, default='', blank=True) 
    created_at = models.CharField(max_length=20, editable=False)
    updated_at = models.CharField(max_length=20, editable=False)

    def get_jalali_date(self):
        current_date = jdatetime.datetime.now()
        return current_date.strftime('%Y/%m/%d')
    
    def save(self, *args, **kwargs):
        if not self.created_at:  
            self.created_at = self.get_jalali_date()
        self.updated_at = self.get_jalali_date()  
        super(Bill, self).save(*args, **kwargs)

    def __str__(self):
        return str (self.customer.name + ": " + str(self.price) + " (" + self.due_date + ")") 

auditlog.register(Bill)
auditlog.register(Factor)