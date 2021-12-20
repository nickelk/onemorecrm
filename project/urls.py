from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    re_path(r'^(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    re_path(r'^update/(?P<pk>\d+)$', views.ProjectUpdateView.as_view(), name='project-update'),
    re_path(r'^delete/(?P<pk>\d+)$', views.ProjectDeleteView.as_view(), name='project-delete'),
]
