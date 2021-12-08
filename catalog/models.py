from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Phone(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    phone = models.CharField(max_length=30, help_text="Phone number")
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.phone


class Email(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    email = models.EmailField(help_text="Email")
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.email


class Customer(models.Model):
    """
    Class defining a model of company(customer).
    """
    company_name = models.CharField(max_length=300, help_text="Company name")
    foreman_name = models.CharField(max_length=300, help_text="Foreman's name")
    description = RichTextField(help_text="Describe the company")
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)
    address = models.CharField(null=True, max_length=300, help_text="Address of the organization")

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.company_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular customer instance.
        """
        return reverse('customer-detail', args=[str(self.id)])

    def get_update_url(self):
        """
        Returns the url to access an updating customer instance.
        """
        return reverse('customer-update', args=[str(self.id)])
