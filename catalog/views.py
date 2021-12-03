# Create your views here.
from django.views import generic
from .models import Customer


class CustomerListView(generic.ListView):
    model = Customer
    paginate_by = 4


class CustomerDetailView(generic.DetailView):
    model = Customer


class CustomerCreate(generic.edit.CreateView):
    model = Customer
    fields = '__all__'


class CustomerUpdate(generic.edit.UpdateView):
    model = Customer
    fields = '__all__'
