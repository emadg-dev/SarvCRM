from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import UserAddForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class SignUpView(LoginRequiredMixin , CreateView):
    form_class = UserAddForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserProfileView(LoginRequiredMixin, TemplateView): 
    template_name = 'userprofile.html'

class UserListView(LoginRequiredMixin, ListView): 
    model =  CustomUser
    template_name= 'userlist.html' 
    paginate_by = 10
    def get_queryset(self): 
        # userid = self.kwargs['id']
        return CustomUser.objects.all()
    