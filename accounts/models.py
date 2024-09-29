from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from auditlog.registry import auditlog

# import django_jalali.db.models as jmodels

from django.contrib.auth.models import Group, Permission, AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # email = models.CharField(max_length=100)

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
    last_name = models.CharField(max_length=30, validators=[persian_regex], default='', blank=True)  

    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',  
        message="شماره تلفن را به درستی وارد کنید."
        )
    phone = models.CharField(max_length=11, validators=[phone_regex], default='')  
    

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='customuser_set',  
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    #     )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='customuser_set',  
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    #     )

    def __str__(self) -> str:
        return str(self.first_name)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})


auditlog.register(CustomUser)
