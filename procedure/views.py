from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import *
from .forms import CustomeraddForm

from django.contrib.auth.mixins import LoginRequiredMixin

class CustomerAddView(LoginRequiredMixin, CreateView): 
    model = Customer
    form_class = CustomeraddForm
    template_name = 'customeradd.html' 
    # fields = ['name','branch', 'SSN', 
    #           'owner', 'address','phone', 
    #           'lock', 'status', 'lead'
    #           ] 
    success_url = reverse_lazy('customerlist')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class CustomerListView(LoginRequiredMixin, ListView): 
    model = Customer 
    template_name= 'customerlist.html' 
    paginate_by = 10
    def get_queryset(self): 
        # userid = self.kwargs['id']
        queryset = []
        if self.request.user.is_staff:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.filter(user=self.request.user)
        
        name = self.request.GET.get('name', None)
        lock = self.request.GET.get('lock', None)
        phone = self.request.GET.get('phone', None)

        # Apply filters to queryset if values are provided
        if name:
            queryset = queryset.filter(name__icontains=name)
        if lock:
            queryset = queryset.filter(lock__icontains=lock)
        if phone:
            queryset = queryset.filter(phone__icontains=phone)

        return queryset
