# Create your views here.
from django.views import generic
from .models import Customer


class CustomerListView(generic.ListView):
    model = Customer
    paginate_by = 4


class CustomerDetailView(generic.DetailView):
    model = Customer
