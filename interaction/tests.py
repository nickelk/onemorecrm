from django.test import TestCase

# Create your tests here.
from catalog.models import Customer
from project.models import Project
from .models import Interaction


class InteractionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(company_name='Big Company', foreman_name='Bob Dylan')
        Project.objects.create(customer_id=1, title='Great Project', price=1000.0)
        Interaction.objects.create(grade=1)

    def test_channel_of_reference_max_length(self):
        interaction = Interaction.objects.get(id=1)
        max_length = interaction._meta.get_field('channel_of_reference').max_length
        self.assertEquals(max_length, 15)

    def test_get_absolute_url(self):
        interaction = Interaction.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(interaction.get_absolute_url(), '/interaction/1')

    def test_get_update_url(self):
        interaction = Interaction.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(interaction.get_update_url(), '/interaction/update/1')

    def test_get_delete_url(self):
        interaction = Interaction.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(interaction.get_delete_url(), '/interaction/delete/1')