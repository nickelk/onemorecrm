from django.urls import path, re_path
from django_filters.views import FilterView
from . import views
from .filters import InteractionFilter

urlpatterns = [
    path('list', views.InteractionListView.as_view(), name='interaction-list'),
    path('mylist', views.MyInteractionsListView.as_view(), name='my-interaction-list'),
    path('search', FilterView.as_view(filterset_class=InteractionFilter), name='search-interaction-list'),
    path('create/', views.InteractionCreateView.as_view(), name='interaction-create'),
    re_path(r'^(?P<pk>\d+)$', views.InteractionDetailView.as_view(), name='interaction-detail'),
    re_path(r'^update/(?P<pk>\d+)$', views.InteractionUpdateView.as_view(), name='interaction-update'),
    re_path(r'^delete/(?P<pk>\d+)$', views.InteractionDeleteView.as_view(), name='interaction-delete'),
]
