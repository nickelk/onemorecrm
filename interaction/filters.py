import django_filters
from .models import Interaction


class InteractionFilter(django_filters.FilterSet):
    class Meta:
        model = Interaction
        fields = {'description': ['icontains'], }
