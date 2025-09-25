from django.test import TestCase
from .models import Vehicle

class VehicleModelTest(TestCase):

    def setUp(self):
        Vehicle.objects.create(make="Toyota", model="Corolla", year=2020, color="Blue")

    def test_vehicle_creation(self):
        vehicle = Vehicle.objects.get(make="Toyota")
        self.assertEqual(vehicle.model, "Corolla")
        self.assertEqual(vehicle.year, 2020)
        self.assertEqual(vehicle.color, "Blue")

    def test_vehicle_str(self):
        vehicle = Vehicle.objects.get(make="Toyota")
        self.assertEqual(str(vehicle), "Toyota Corolla")  # Assuming __str__ method is defined in the model

    def test_vehicle_year(self):
        vehicle = Vehicle.objects.get(make="Toyota")
        self.assertTrue(vehicle.year >= 2000)  # Check if the year is valid

    def test_vehicle_color(self):
        vehicle = Vehicle.objects.get(make="Toyota")
        self.assertIn(vehicle.color, ["Red", "Blue", "Black", "White"])  # Check if color is one of the expected values