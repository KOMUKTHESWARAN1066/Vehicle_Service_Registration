from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'mobile_number']  # Update these fields to match your model
    ordering = ['id']  # Update this field to match your model
    list_filter = ['date_joined']  # Update this field to match your model

admin.site.register(Customer, CustomerAdmin)