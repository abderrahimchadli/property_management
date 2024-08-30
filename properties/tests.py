from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Property, Tenant, RentalPayment
from datetime import date

User = get_user_model()

class PropertyManagementTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='testuser@example.com', 
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

        self.property = Property.objects.create(
            name='Test Property',
            address='123 Test St',
            property_type='Apartment',
            number_of_units=5,
            rental_cost=1000.00
        )

        self.tenant = Tenant.objects.create(
            property=self.property,
            name='John Doe',
            contact_details='john@example.com',
            unit='101'
        )

    def test_create_property(self):
        data = {
            'name': 'New Property',
            'address': '456 New St',
            'property_type': 'House',
            'number_of_units': 1,
            'rental_cost': 1500.00
        }
        response = self.client.post('/api/properties/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 2)

    def test_get_properties(self):
        response = self.client.get('/api/properties/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_tenant(self):
        data = {
            'property': self.property.id,
            'name': 'Jane Smith',
            'contact_details': 'jane@example.com',
            'unit': '102'
        }
        response = self.client.post('/api/tenants/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 2)

    def test_create_rental_payment(self):
        data = {
            'tenant': self.tenant.id,
            'amount': 1000.00,
            'payment_date': str(date.today()),
            'is_paid': True
        }
        response = self.client.post('/api/payments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RentalPayment.objects.count(), 1)

    def test_property_filter(self):
        response = self.client.get('/api/properties/?property_type=Apartment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        response = self.client.get('/api/properties/?property_type=House')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_property_ordering(self):
        Property.objects.create(
            name='A Property',
            address='789 A St',
            property_type='House',
            number_of_units=1,
            rental_cost=2000.00
        )
        response = self.client.get('/api/properties/?ordering=name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'A Property')

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/properties/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
