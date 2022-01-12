from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, TemplateView

from .forms import RegisterUserForm
from .models import OwnCabinet
from django.shortcuts import get_object_or_404


class OwnCabinetDetailView(LoginRequiredMixin, DetailView):
    """
    Generic class-based view of user's own cabinet
    """
    model = OwnCabinet
    
    def setup(self, request, *args, **kwargs):
        """
        Getting current user's id
        """
        self.user_id = request.user.pk
        return super(OwnCabinetDetailView, self).setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Set pk as current user's id
        """
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class OwnCabinetUpdateView(LoginRequiredMixin, UpdateView):
    """
    Generic class-based view updating user's own cabinet
    """
    model = OwnCabinet
    fields = ['username', 'avatar', 'first_name', 'last_name', 'email']

    def setup(self, request, *args, **kwargs):
        """
        Getting current user's id
        """
        self.user_id = request.user.pk
        return super(OwnCabinetUpdateView, self).setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Set pk as current user's id
        """
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class RegisterUserView(CreateView):
    model = OwnCabinet
    template_name = 'registration/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register-done')


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
