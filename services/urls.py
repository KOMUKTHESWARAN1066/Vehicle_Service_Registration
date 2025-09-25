from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.service_registration, name='service_registration'),
    path('register/', views.service_registration, name='register_service'),
    path('manage/', views.manage_services, name='manage_services'),
]