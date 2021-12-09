# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Customer, Phone, Email


class CustomerListView(LoginRequiredMixin, ListView):
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


class CustomerDetailView(LoginRequiredMixin, DetailView):
    login_url = 'accounts/login'
    model = Customer

    # def get_context_data(self, **kwargs):
    #     context = super(CustomerDetailView, self).get_context_data(**kwargs)
    #     print(context['object'])
    #     return context


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        """
        Add formsets into context
        """
        PhoneInlineFormSet = inlineformset_factory(Customer, Phone, fields=('phone',), can_delete=True, extra=1)
        EmailInlineFormSet = inlineformset_factory(Customer, Email, fields=('email',), can_delete=True, extra=1)
        context = super(CustomerCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['phone_formset'] = PhoneInlineFormSet(self.request.POST, instance=self.object)
            context['phone_formset'].full_clean()
            context['email_formset'] = EmailInlineFormSet(self.request.POST, instance=self.object)
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneInlineFormSet(instance=self.object)
            context['email_formset'] = EmailInlineFormSet(instance=self.object)
        # print(context['phone_formset'])
        return context


class CustomerUpdateView(UpdateView):

    model = Customer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        """
        Add formsets into context
        """
        PhoneInlineFormSet = inlineformset_factory(Customer, Phone, fields=('phone',), can_delete=True, extra=1)
        EmailInlineFormSet = inlineformset_factory(Customer, Email, fields=('email',), can_delete=True, extra=1)
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['phone_formset'] = PhoneInlineFormSet(self.request.POST, instance=self.object)
            context['phone_formset'].full_clean()
            context['email_formset'] = EmailInlineFormSet(self.request.POST, instance=self.object)
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneInlineFormSet(instance=self.object)
            context['email_formset'] = EmailInlineFormSet(instance=self.object)
        # print(context['phone_formset'])
        return context

    def form_valid(self, form):
        """
        Check formset validity and save it
        """
        context = self.get_context_data(form=form)
        formsets = [context['phone_formset'], context['email_formset']]
        for formset in formsets:
            if formset.is_valid():
                formset.save(commit=False)
                return super().form_valid(form)
            else:
                return super().form_invalid(form)

