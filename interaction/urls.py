from django.conf.urls import url
from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import InteractionFilter

urlpatterns = [
    path('list', views.InteractionListView.as_view(), name='interaction-list'),
    path('mylist', views.MyInteractionsListView.as_view(), name='my-interaction-list'),
    path('search', FilterView.as_view(filterset_class=InteractionFilter), name='search-interaction-list'),
    path('create/', views.InteractionCreateView.as_view(), name='interaction-create'),
    url(r'^(?P<pk>\d+)$', views.InteractionDetailView.as_view(), name='interaction-detail'),
    url(r'^update/(?P<pk>\d+)$', views.InteractionUpdateView.as_view(), name='interaction-update'),
    url(r'^delete/(?P<pk>\d+)$', views.InteractionDeleteView.as_view(), name='interaction-delete'),
]
