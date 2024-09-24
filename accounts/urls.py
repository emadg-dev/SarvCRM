from django.urls import path 
from .views import *

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='userprofile'),
    path('userlist/', UserListView.as_view(), name='userlist'),    
]
