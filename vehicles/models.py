from django.db import models

class Vehicle(models.Model):
    MAKE_CHOICES = [
        ('Yamaha', 'Yamaha'),
        ('Honda', 'Honda'),
        ('Suzuki', 'Suzuki'),
        ('Bajaj', 'Bajaj'),
        ('TVS', 'TVS'),
    ]

    model = models.CharField(max_length=100)
    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicles/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.vehicle.registration_number}"

class VehicleAudio(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='audio_records')
    audio_file = models.FileField(upload_to='vehicles/audio/')
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio for {self.vehicle.registration_number}"