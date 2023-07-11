from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls, name=''),
      path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]
