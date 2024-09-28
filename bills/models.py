from django.db import models
from accounts.models import CustomUser

    
# class Customer(models.Model):
#     user = models.ForeignKey(CustomUser,
#             on_delete=models.PROTECT)
#     # product = models.ForeignKey(Stock, 
#             # on_delete=models.CASCADE)
#     #quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    
#     owner = models.CharField(max_length=50, )