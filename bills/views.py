from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from crm.CustomMixines import StaffRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin

class BillListView(LoginRequiredMixin, ListView): 
    model = Bill 
    template_name = 'billlist.html' 
    paginate_by = 10

    def get_queryset(self): 
        queryset = []
        
        if self.request.user.is_staff:
            queryset = Bill.objects.all()
        else:
            queryset = Bill.objects.filter(user=self.request.user)

        # id = self.request.GET.get('id', None)
        # customer = self.request.GET.get('customer', None)
        # status = self.request.GET.get('status', None)
        # user = self.request.GET.get('user', None)
        # comment = self.request.GET.get('comment', None)

        
        # if id:
        #     queryset = queryset.filter(id__icontains=id)
        # if customer:
        #     queryset = queryset.filter(customer__icontains=customer)
        # if status:
        #     queryset = queryset.filter(status__icontains=status)
        # if user:
        #     queryset = queryset.filter(user__first_name__icontains=user) 
        # if comment:
        #     queryset = queryset.filter(comment__icontains=comment)

        # sort_field = self.request.GET.get('sort', 'id')  
        # sort_order = self.request.GET.get('order', 'asc')  

        # valid_sort_fields = ['id', 'customer', 'status', 'user', 'created_at', 'updated_at', 'comment']
        # if sort_field not in valid_sort_fields:
        #     sort_field = 'id'  

        # if sort_order == 'desc':
        #     queryset = queryset.order_by(f'-{sort_field}')  
        # else:
        #     queryset = queryset.order_by(sort_field) 

        return queryset.order_by('-id')

class BillAddView(LoginRequiredMixin, CreateView): 
    model = Bill
    form_class = BilladdForm
    template_name = 'billadd.html' 
    # fields = ['name','branch', 'SSN', 
    #           'owner', 'address','phone', 
    #           'lock', 'status', 'lead'
    #           ] 
    success_url = reverse_lazy('billlist')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    

class BillUpdateView(LoginRequiredMixin, UpdateView): 
    model = Bill 
    template_name = 'billupdate.html' 
    form_class = BillUpdateForm
    success_url = reverse_lazy('billlist') 


class BillDeleteView(StaffRequiredMixin, DeleteView): 
    model = Bill 
    template_name = 'billdelete.html' 
    fields = "__all__" 
    success_url = reverse_lazy('billlist') 



class FactorListView(LoginRequiredMixin, ListView): 
    model = Factor 
    template_name = 'factorlist.html' 
    paginate_by = 10

    def get_queryset(self): 
        queryset = []
        
        if self.request.user.is_staff:
            queryset = Factor.objects.all()
        else:
            queryset = Factor.objects.filter(user=self.request.user)

        # id = self.request.GET.get('id', None)
        # customer = self.request.GET.get('customer', None)
        # status = self.request.GET.get('status', None)
        # user = self.request.GET.get('user', None)
        # comment = self.request.GET.get('comment', None)

        
        # if id:
        #     queryset = queryset.filter(id__icontains=id)
        # if customer:
        #     queryset = queryset.filter(customer__icontains=customer)
        # if status:
        #     queryset = queryset.filter(status__icontains=status)
        # if user:
        #     queryset = queryset.filter(user__first_name__icontains=user) 
        # if comment:
        #     queryset = queryset.filter(comment__icontains=comment)

        # sort_field = self.request.GET.get('sort', 'id')  
        # sort_order = self.request.GET.get('order', 'asc')  

        # valid_sort_fields = ['id', 'customer', 'status', 'user', 'created_at', 'updated_at', 'comment']
        # if sort_field not in valid_sort_fields:
        #     sort_field = 'id'  

        # if sort_order == 'desc':
        #     queryset = queryset.order_by(f'-{sort_field}')  
        # else:
        #     queryset = queryset.order_by(sort_field) 

        return queryset.order_by('-id')

class FactorAddView(LoginRequiredMixin, CreateView): 
    model = Factor
    form_class = FactoraddForm
    template_name = 'factoradd.html' 
    # fields = ['name','branch', 'SSN', 
    #           'owner', 'address','phone', 
    #           'lock', 'status', 'lead'
    #           ] 
    success_url = reverse_lazy('factorlist')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    

class FactorUpdateView(LoginRequiredMixin, UpdateView): 
    model = Factor 
    template_name = 'factorupdate.html' 
    form_class = FactorUpdateForm
    success_url = reverse_lazy('factorlist') 


class FactorDeleteView(StaffRequiredMixin, DeleteView): 
    model = Factor 
    template_name = 'factordelete.html' 
    fields = "__all__" 
    success_url = reverse_lazy('factorlist') 

