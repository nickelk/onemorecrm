from django.test import TestCase

# Create your tests here.
from owncabinet.models import OwnCabinet
from .models import Customer
from django.urls import reverse


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


class CustomerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = OwnCabinet.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        # Create 13 customers for pagination tests
        number_of_customers = 13
        for company_num in range(number_of_customers):
            Customer.objects.create(company_name='Company %s' % company_num,
                                    foreman_name='Foreman %s' % company_num, )

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/customer_list.html')

    def test_pagination_is_five(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['customer_list']) == 5)

    def test_lists_all_customers(self):
        self.client.login(username='john', password='johnpassword')
        # Get third page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('home') + '?page=3')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['customer_list']) == 3)
