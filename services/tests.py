from django.test import TestCase
from .models import Service, ServiceType, ServicePackage

class ServiceModelTests(TestCase):

    def setUp(self):
        self.service_type = ServiceType.objects.create(name="General Service")
        self.service_package = ServicePackage.objects.create(name="Basic Package", price=1000)

    def test_service_creation(self):
        service = Service.objects.create(
            service_type=self.service_type,
            service_package=self.service_package,
            customer_name="John Doe",
            vehicle_registration_number="ABC1234",
            additional_requirements="Oil change and tire rotation"
        )
        self.assertEqual(service.customer_name, "John Doe")
        self.assertEqual(service.vehicle_registration_number, "ABC1234")
        self.assertEqual(service.additional_requirements, "Oil change and tire rotation")
        self.assertEqual(service.service_type.name, "General Service")
        self.assertEqual(service.service_package.name, "Basic Package")

    def test_service_type_str(self):
        self.assertEqual(str(self.service_type), "General Service")

    def test_service_package_str(self):
        self.assertEqual(str(self.service_package), "Basic Package")