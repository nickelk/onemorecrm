from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import MyProfile


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = MyProfile
