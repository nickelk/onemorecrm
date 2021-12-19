from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    url(r'^(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^update/(?P<pk>\d+)$', views.ProjectUpdateView.as_view(), name='project-update'),
    url(r'^delete/(?P<pk>\d+)$', views.ProjectDeleteView.as_view(), name='project-delete'),
]
