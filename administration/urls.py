from django.urls import path 
from .views import *

urlpatterns = [
    path('panel/', AdminPanelView.as_view(), name='adminpanel'),
]