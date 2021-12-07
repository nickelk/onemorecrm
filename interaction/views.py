from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
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
