from django.urls import path 
from .views import *

urlpatterns = [
    
    path('customer-list/', CustomerListView.as_view(), name='customerlist'),
    path('customer-add/', CustomerAddView.as_view(), name='customeradd'),
    path('customer-delete/<int:pk>', CustomerDeleteView.as_view(), name='customerdelete'),
    path('customer-update/<int:pk>', CustomerUpdateView.as_view(), name='customerupdate'),
    path('procedure-list/', ProcedureListView.as_view(), name='procedurelist'),
    path('procedure-add/', ProcedureAddView.as_view(), name='procedureadd'),
    path('procedure-update/<int:pk>', ProcedureUpdateView.as_view(), name='procedureupdate'),
    path('demo-list/', DemoListView.as_view(), name='demolist'),
    path('demo-add/', DemoAddView.as_view(), name='demoadd'),
    path('demo-delete/<int:pk>', DemoDeleteView.as_view(), name='demodelete'),
    path('demo-update/<int:pk>', DemoUpdateView.as_view(), name='demoupdate'),
]

