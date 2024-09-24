from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminPanelView(LoginRequiredMixin, TemplateView): 
     template_name = 'adminpanel.html'

