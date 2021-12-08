from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views import generic
from .models import Interaction


# Create your views here.
class InteractionListView(PermissionRequiredMixin, generic.ListView):
    permission_required = ''
    model = Interaction
    paginate_by = 4


class InteractionDetailView(generic.DetailView):
    model = Interaction


class InteractionCreate(generic.edit.CreateView):
    model = Interaction
    fields = '__all__'


class InteractionUpdate(generic.edit.UpdateView):
    model = Interaction
    fields = '__all__'


class MyInteractionsListView(PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing interactions, created by current user.
    """
    permission_required = ''
    model = Interaction
    template_name = 'interaction/interaction_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Interaction.objects.filter(manager=self.request.user).order_by('date_of_edition')
