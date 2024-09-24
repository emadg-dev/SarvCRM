from django.urls import path 
from .views import *

urlpatterns = [
    
    path('customer-add/', CustomerAddView.as_view(), name='customeradd'),
    path('customer-list/', CustomerListView.as_view(), name='customerlist'),

]

