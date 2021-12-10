from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 4


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'project.add_project'
    model = Project
    fields = '__all__'


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'project.change_project'
    model = Project
    fields = '__all__'
