# Create your views here.
from django.views import generic
from .models import Customer


class CustomerListView(generic.ListView):

    model = Customer
    paginate_by = 5


class CustomerDetailView(generic.DetailView):
    model = Customer