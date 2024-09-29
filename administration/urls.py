from django.urls import path 
from .views import *

urlpatterns = [
    path('panel/', AdminPanelView.as_view(), name='adminpanel'),
    path('userupdate/<int:pk>', UserUpdateView.as_view(), name='userupdate'),
]