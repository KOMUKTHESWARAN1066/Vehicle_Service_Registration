from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm



def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)  # This will return 404 if not found
    customer.delete()
    return redirect('list_customers')

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_customers)
    else:
        form = CustomerForm()
    return render(request, 'customers/register_customer.html', {'form': form})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    print(1)
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})