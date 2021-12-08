from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.InteractionListView.as_view(), name='interaction-list'),
    path('mylist', views.MyInteractionsListView.as_view(), name='my-interaction-list'),
    path('create/', views.InteractionCreate.as_view(), name='interaction-create'),
    url(r'^(?P<pk>\d+)$', views.InteractionDetailView.as_view(), name='interaction-detail'),
    url(r'^update/(?P<pk>\d+)$', views.InteractionUpdate.as_view(), name='interaction-update'),
]
