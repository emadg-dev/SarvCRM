from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from django.contrib.auth.mixins import LoginRequiredMixin

class dashboardView(LoginRequiredMixin, TemplateView):
    
    template_name= 'dashboard.html'