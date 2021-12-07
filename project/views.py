from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Project


class ProjectListView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts/login'
    model = Project
    paginate_by = 4


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts/login'
    model = Project


class ProjectCreate(generic.edit.CreateView):
    model = Project
    fields = '__all__'


class ProjectUpdate(generic.edit.UpdateView):
    model = Project
    fields = '__all__'
