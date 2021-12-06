# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from .models import Customer, Project, Interaction


class CustomerListView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login'
    model = Customer
    paginate_by = 4

    def get_queryset(self):
        try:
            if self.request.GET['order'] == '-company_name':
                order = '-company_name'
            elif self.request.GET['order'] == 'date_of_creation':
                order = 'date_of_creation'
            elif self.request.GET['order'] == '-date_of_creation':
                order = '-date_of_creation'
            else:
                order = 'company_name'
        except MultiValueDictKeyError:
            order = 'company_name'
        return Customer.objects.order_by(order)


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login'
    model = Customer


class CustomerCreate(generic.edit.CreateView):
    model = Customer
    fields = '__all__'


class CustomerUpdate(generic.edit.UpdateView):
    model = Customer
    fields = '__all__'


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 4


class ProjectDetailView(generic.DetailView):
    model = Project


class ProjectCreate(generic.edit.CreateView):
    model = Project
    fields = '__all__'


class ProjectUpdate(generic.edit.UpdateView):
    model = Project
    fields = '__all__'


class InteractionListView(generic.ListView):
    model = Interaction
    paginate_by = 4


class InteractionDetailView(generic.DetailView):
    model = Interaction


class InteractionCreate(generic.edit.CreateView):
    model = Interaction
    fields = '__all__'


class InteractionUpdate(generic.edit.UpdateView):
    model = Interaction
    fields = '__all__'
