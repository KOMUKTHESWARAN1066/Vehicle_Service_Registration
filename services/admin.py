from django.contrib import admin
from .models import ServiceType, ServicePackage, ServiceBooking

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_type', 'description', 'created_at')
    search_fields = ('service_type', 'description')

class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'package_name', 'price', 'services_included')
    search_fields = ('package_name',)

admin.site.register(ServiceType)
admin.site.register(ServicePackage)
admin.site.register(ServiceBooking)