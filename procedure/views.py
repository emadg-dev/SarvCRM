from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from crm.CustomMixines import StaffRequiredMixin

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
        owner = self.request.GET.get('owner', None)
        status = self.request.GET.get('status', None)
        lead = self.request.GET.get('lead', None)

        # Apply filters to queryset if values are provided
        if name:
            queryset = queryset.filter(name__icontains=name)
        if lock:
            queryset = queryset.filter(lock__icontains=lock)
        if phone:
            queryset = queryset.filter(phone__icontains=phone)
        if owner:
            queryset = queryset.filter(owner__icontains=owner)
        if status:
            queryset = queryset.filter(status__icontains=status)
        if lead:
            queryset = queryset.filter(lead__icontains=lead)

        return queryset


class CustomerDeleteView(StaffRequiredMixin, DeleteView): 
    model = Customer 
    template_name = 'customerdelete.html' 
    fields = "__all__" 
    success_url = reverse_lazy('customerlist') 


class CustomerUpdateView(LoginRequiredMixin, UpdateView): 
    model = Customer 
    template_name = 'customerupdate.html' 
    form_class = CustomerUpdateForm
    success_url = reverse_lazy('customerlist') 

class ProcedureListView(LoginRequiredMixin, ListView): 
    model = Procedure 
    template_name = 'procedurelist.html' 
    paginate_by = 10

    def get_queryset(self): 
        queryset = []
        
        if self.request.user.is_staff:
            queryset = Procedure.objects.all()
        else:
            queryset = Procedure.objects.filter(user=self.request.user)

        # Get filter values from the request
        id = self.request.GET.get('id', None)
        customer = self.request.GET.get('customer', None)
        status = self.request.GET.get('status', None)
        user = self.request.GET.get('user', None)
        comment = self.request.GET.get('comment', None)

        # Apply filters to queryset if values are provided
        if id:
            queryset = queryset.filter(id__icontains=id)
        if customer:
            queryset = queryset.filter(customer__icontains=customer)
        if status:
            queryset = queryset.filter(status__icontains=status)
        if user:
            queryset = queryset.filter(user__first_name__icontains=user)  # Use appropriate field for filtering
        if comment:
            queryset = queryset.filter(comment__icontains=comment)

        # Get sort field and order from the request
        sort_field = self.request.GET.get('sort', 'id')  # Default sort field
        sort_order = self.request.GET.get('order', 'asc')  # Default sort order

        # Validate the sort field
        valid_sort_fields = ['id', 'customer', 'status', 'user', 'created_at', 'updated_at', 'comment']
        if sort_field not in valid_sort_fields:
            sort_field = 'id'  # Fallback to default field if invalid

        # Toggle sort order
        if sort_order == 'desc':
            queryset = queryset.order_by(f'-{sort_field}')  # Descending order
        else:
            queryset = queryset.order_by(sort_field)  # Ascending order

        return queryset

class ProcedureAddView(LoginRequiredMixin, CreateView): 
    model = Procedure
    form_class = ProcedureaddForm
    template_name = 'procedureadd.html' 
    # fields = ['name','branch', 'SSN', 
    #           'owner', 'address','phone', 
    #           'lock', 'status', 'lead'
    #           ] 
    success_url = reverse_lazy('procedurelist')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    

class ProcedureUpdateView(LoginRequiredMixin, UpdateView): 
    model = Procedure 
    template_name = 'procedureupdate.html' 
    form_class = ProcedureUpdateForm
    success_url = reverse_lazy('procedurelist') 
