from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.OwnCabinetDetailView.as_view(), name='owncabinet'),
    url(r'^update/(?P<pk>\d+)$', views.OwnCabinetUpdateView.as_view(), name='owncabinet-update'),
]
