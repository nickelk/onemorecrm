from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Interaction
from django.urls import reverse_lazy


class InteractionListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing interactions
    """
    permission_required = 'interaction.view_interaction'
    model = Interaction
    paginate_by = 4


class InteractionDetailView(PermissionRequiredMixin, DetailView):
    """
    Generic class-based view detailing interactions
    """
    permission_required = 'interaction.view_interaction'
    model = Interaction


class InteractionCreateView(PermissionRequiredMixin, CreateView):
    """
    Generic class-based view creating interactions
    """
    permission_required = 'interaction.add_interaction'
    model = Interaction
    fields = '__all__'


class InteractionUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Generic class-based view updating interactions
    """
    permission_required = 'interaction.change_interaction'
    model = Interaction
    fields = '__all__'


class InteractionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Generic class-based view deleting interactions
    """
    permission_required = 'interaction.delete_interaction'
    model = Interaction
    success_url = reverse_lazy('search-interaction-list')


class MyInteractionsListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing interactions, created by current user.
    """
    permission_required = 'interaction.view_interaction'
    template_name = 'interaction/my_interaction_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Filtered by manager queryset
        """
        return Interaction.objects.filter(manager=self.request.user).order_by('date_of_edition')
