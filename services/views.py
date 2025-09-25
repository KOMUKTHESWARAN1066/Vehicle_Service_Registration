from django.shortcuts import render, redirect
from .models import ServiceType, ServicePackage, ServiceBooking
from .forms import ServiceForm, ServiceTypeForm, ServicePackageForm

def service_registration(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_success')
    else:
        form = ServiceForm()
    return render(request, 'services/book_service.html', {'form': form})

def service_success(request):
    return render(request, 'services/service_success.html')

# Add the manage_services view function
def manage_services(request):
    services = ServiceBooking.objects.all()
    return render(request, 'services/manage_services.html', {'services': services})