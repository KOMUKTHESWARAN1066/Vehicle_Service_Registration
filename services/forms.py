from django import forms
from .models import ServiceType, ServicePackage, ServiceBooking

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['vehicle', 'service_type', 'service_package', 'additional_requirements']

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['name', 'description']

class ServicePackageForm(forms.ModelForm):
    class Meta:
        model = ServicePackage
        fields = ['service_type', 'name', 'price']