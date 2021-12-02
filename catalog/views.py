# Create your views here.
from django.views.generic import ListView
from .models import Customer


class CustomerListView(ListView):

    model = Customer
    paginate_by = 5
