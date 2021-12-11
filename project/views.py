from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 4


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'project.add_project'
    model = Project
    fields = '__all__'


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'project.change_project'
    model = Project
    fields = '__all__'


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'project.delete_project'
    model = Project
    success_url = reverse_lazy('project-list')
