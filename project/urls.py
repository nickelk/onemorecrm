from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreate.as_view(), name='project-create'),
    url(r'^(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^update/(?P<pk>\d+)$', views.ProjectUpdate.as_view(), name='project-update'),
]
