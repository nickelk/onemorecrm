from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import OwnCabinet
from  django.shortcuts import get_object_or_404


class OwnCabinetDetailView(LoginRequiredMixin, DetailView):
    model = OwnCabinet
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(OwnCabinetDetailView, self).setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class OwnCabinetUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnCabinet
    fields = ['username', 'avatar', 'first_name', 'last_name', 'email']

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(OwnCabinetUpdateView, self).setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
