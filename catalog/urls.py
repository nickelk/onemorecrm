"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='home'),
    path('customer/create/', views.CustomerCreateView.as_view(), name='customer-create'),
    re_path(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer-detail'),
    re_path(r'^customer/update/(?P<pk>\d+)$', views.CustomerUpdateView.as_view(), name='customer-update'),
    re_path(r'^customer/delete/(?P<pk>\d+)$', views.CustomerDeleteView.as_view(), name='customer-delete'),
]
