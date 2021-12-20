from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing projects
    """
    model = Project
    paginate_by = 5


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """
    Generic class-based view detailing project
    """
    model = Project


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    """
    Generic class-based view creating project
    """
    permission_required = 'project.add_project'
    model = Project
    fields = '__all__'


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Generic class-based view updating project
    """
    permission_required = 'project.change_project'
    model = Project
    fields = '__all__'


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Generic class-based view deleting project
    """
    permission_required = 'project.delete_project'
    model = Project
    success_url = reverse_lazy('project-list')
