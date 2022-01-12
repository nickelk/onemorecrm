from django.urls import path
from . import views

urlpatterns = [
    path('', views.OwnCabinetDetailView.as_view(), name='owncabinet'),
    path('update/', views.OwnCabinetUpdateView.as_view(), name='owncabinet-update'),
    path('register/', views.RegisterUserView.as_view(), name='register-user'),
    path('register/done', views.RegisterDoneView.as_view(), name='register-done'),
]
