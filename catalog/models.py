from datetime import date

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Phone(models.Model):
    """
    Class defining a model, derived from the Model class.
    """
    phone = models.CharField(max_length=30, help_text="Phone number")

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
    phone = models.ManyToManyField(Phone, help_text="Phone number(s)")
    email = models.ManyToManyField(Email, help_text="Email(s)")

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


class Project(models.Model):
    """
    Class defining a model of project.
    """
    title = models.CharField(max_length=300, help_text="Project title")
    description = RichTextField(help_text="Describe the project")
    begin_date = models.DateField(default=date.today, help_text="Project start date")
    end_date = models.DateField(null=True, blank=True, help_text="Project end date")
    price = models.FloatField()

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.title


class Interaction(models.Model):
    """
    Class defining a model of interaction between customer and contractor.
    """
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    CHANNEL = (
        ('r', 'Request'),
        ('l', 'Letter'),
        ('w', 'Web site'),
        ('c', 'Company init.'),
    )

    channel_of_reference = models.CharField(max_length=1,
                                            choices=CHANNEL,
                                            blank=True,
                                            default='r',
                                            help_text='Interaction way')

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = RichTextField(help_text="Describe the interaction")

    GRADES = ((-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, '-1'),
              (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

    grade = models.DecimalField(decimal_places=2,
                                max_digits=2,
                                choices=GRADES,
                                blank=True,
                                default=1,
                                help_text='Interaction grade')

    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'Proj.: %s, Comp.: %s' % (self.project, self.company)
