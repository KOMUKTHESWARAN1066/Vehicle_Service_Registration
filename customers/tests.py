from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            address="123 Main St",
            mobile_no="1234567890",
            alt_contact_no="0987654321"
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.address, "123 Main St")
        self.assertEqual(self.customer.mobile_no, "1234567890")
        self.assertEqual(self.customer.alt_contact_no, "0987654321")

    def test_customer_str(self):
        self.assertEqual(str(self.customer), "John Doe")