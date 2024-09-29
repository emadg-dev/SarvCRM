from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from crm.CustomMixines import StaffRequiredMixin
from accounts.models import CustomUser
from .forms import UserUpdateForm


class AdminPanelView(StaffRequiredMixin, TemplateView): 
     template_name = 'adminpanel.html'

class UserUpdateView(StaffRequiredMixin, UpdateView): 
    model = CustomUser 
    template_name = 'userupdate.html' 
    form_class = UserUpdateForm
    success_url = reverse_lazy('userlist') 
