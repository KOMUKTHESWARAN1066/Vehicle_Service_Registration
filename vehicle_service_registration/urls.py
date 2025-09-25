from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customers.urls')),
    path('services/', include('services.urls')),
    path('register/', include('vehicles.urls')),
    ]