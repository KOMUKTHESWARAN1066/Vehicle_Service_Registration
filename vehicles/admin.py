from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'color')
    search_fields = ('make', 'model', 'year', 'color')
    list_filter = ('make', 'year', 'color')

admin.site.register(Vehicle, VehicleAdmin)