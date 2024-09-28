from django.urls import path 
from .views import *

urlpatterns = [
    
    path('customer-add/', CustomerAddView.as_view(), name='customeradd'),
    path('customer-list/', CustomerListView.as_view(), name='customerlist'),
    path('customerdelete/<int:pk>', CustomerDeleteView.as_view(), name='customerdelete'),
    path('customerupdate/<int:pk>', CustomerUpdateView.as_view(), name='customerupdate'),

]

