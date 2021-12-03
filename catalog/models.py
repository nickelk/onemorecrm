from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Phone(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    phone = models.CharField(max_length=30, help_text="Enter phone number")

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.phone


class Email(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    email = models.EmailField(help_text="Enter email")

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.email


class Customer(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    company_name = models.CharField(max_length=300, help_text="Enter company name")
    foreman_name = models.CharField(max_length=300, help_text="Enter foreman's name")
    descriptions = RichTextField(help_text="Describe the company")
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)
    adress = models.CharField(max_length=300, help_text="Enter the adress of the organization")
    phone = models.ManyToManyField(Phone, help_text="Enter phone number")
    email = models.ManyToManyField(Email, help_text="Enter email")

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.company_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('customer-detail', args=[str(self.id)])
