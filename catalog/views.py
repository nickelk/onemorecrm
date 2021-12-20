from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer, Phone, Email


class CustomerListView(LoginRequiredMixin, ListView):
    """
    View, inherited from generic class
    """
    login_url = 'accounts/login'
    paginate_by = 5

    def get_queryset(self):
        """
        Make ordered queryset
        """
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
    """
    View, inherited from generic class
    """
    login_url = 'accounts/login'
    model = Customer


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """
    View, inherited from generic class
    """
    permission_required = 'customer.add_customer'
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
            context['phone_formset'] = PhoneInlineFormSet(self.request.POST, instance=self.object, prefix='phones')
            context['phone_formset'].full_clean()
            context['email_formset'] = EmailInlineFormSet(self.request.POST, instance=self.object, prefix='emails')
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneInlineFormSet(instance=self.object, prefix='phones')
            context['email_formset'] = EmailInlineFormSet(instance=self.object, prefix='emails')
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
            else:
                return super().form_invalid(form)
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    """
    View, inherited from generic class
    """
    permission_required = 'customer.change_customer'
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
            context['phone_formset'] = PhoneInlineFormSet(self.request.POST, instance=self.object, prefix='phones')
            context['phone_formset'].full_clean()
            context['email_formset'] = EmailInlineFormSet(self.request.POST, instance=self.object, prefix='emails')
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneInlineFormSet(instance=self.object, prefix='phones')
            context['email_formset'] = EmailInlineFormSet(instance=self.object, prefix='emails')
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
            else:
                return super().form_invalid(form)
        return super().form_valid(form)


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View, inherited from generic class
    """
    permission_required = 'customer.delete_customer'
    model = Customer
    success_url = reverse_lazy('home')
