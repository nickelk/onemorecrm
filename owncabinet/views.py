from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import OwnCabinet


class OwnCabinetDetailView(LoginRequiredMixin, DetailView):
    model = OwnCabinet
