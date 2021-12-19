from django.test import TestCase

# Create your tests here.
from .models import Customer


class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(company_name='Big Company', foreman_name='Bob Dylan')

    def test_company_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('company_name').max_length
        self.assertEquals(max_length, 300)

    def test_foreman_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('foreman_name').max_length
        self.assertEquals(max_length, 300)

    def test_address_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('address').max_length
        self.assertEquals(max_length, 300)

    def test_get_absolute_url(self):
        customer = Customer.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(customer.get_absolute_url(), '/customer/1')

    def test_get_update_url(self):
        customer = Customer.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(customer.get_update_url(), '/customer/update/1')

    def test_get_delete_url(self):
        customer = Customer.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(customer.get_delete_url(), '/customer/delete/1')
