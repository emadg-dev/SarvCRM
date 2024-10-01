from django.urls import path 
from .views import *

urlpatterns = [
    path('bill-list/', BillListView.as_view(), name='billlist'),
    path('bill-add/', BillAddView.as_view(), name='billadd'),
    path('bill-delete/<int:pk>', BillDeleteView.as_view(), name='billdelete'),
    path('bill-update/<int:pk>', BillUpdateView.as_view(), name='billupdate'),
    path('factor-list/', FactorListView.as_view(), name='factorlist'),
    path('factor-add/', FactorAddView.as_view(), name='factoradd'),
    path('factor-delete/<int:pk>', FactorDeleteView.as_view(), name='factordelete'),
    path('factor-update/<int:pk>', FactorUpdateView.as_view(), name='factorupdate'),
]