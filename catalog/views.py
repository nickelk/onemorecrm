# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Customer
from django.urls import reverse


class CustomerListView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login'
    model = Customer
    paginate_by = 4


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login'
    model = Customer


class CustomerCreate(generic.edit.CreateView):
    model = Customer
    fields = '__all__'


class CustomerUpdate(generic.edit.UpdateView):
    model = Customer
    fields = '__all__'
