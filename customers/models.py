from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)  # Add this field
    address = models.TextField()  # Add this field
    alternate_number = models.CharField(max_length=15, blank=True, null=True)  # Add this field
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"