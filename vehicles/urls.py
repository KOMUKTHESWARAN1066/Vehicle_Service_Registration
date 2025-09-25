from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('list/', views.vehicle_list, name='vehicle_list'),
    path('register', views.vehicle_create, name='vehicle_create'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('<int:pk>/edit/', views.vehicle_update, name='vehicle_update'),
    path('<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
]