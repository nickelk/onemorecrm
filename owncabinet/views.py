from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import OwnCabinet


class OwnCabinetDetailView(LoginRequiredMixin, DetailView):
    model = OwnCabinet


class OwnCabinetUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnCabinet
    fields = ['username', 'avatar', 'first_name', 'last_name', 'email']
