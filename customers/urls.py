from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('register', views.register_customer, name='register_customer'),
    path('list/', views.list_customers, name='list_customers'),
    path('detail/<int:id>/', views.customer_detail, name='customer_detail'),
    path('update/<int:pk>/', views.customer_update, name='customer_update'),
    path('edit/<int:pk>/', views.customer_update, name='edit_customer'),
    path('delete/<int:pk>/', views.customer_delete, name='delete_customer'),
]