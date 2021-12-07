from django.db import models
from django.contrib.auth.models import User
from project.models import Project
from catalog.models import Customer
from ckeditor.fields import RichTextField


# Create your models here.
class Interaction(models.Model):
    """
    Class defining a model of interaction between customer and contractor.
    """
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    CHANNEL = (
        ('Request', 'Request'),
        ('Letter', 'Letter'),
        ('Web site', 'Web site'),
        ('Company init.', 'Company initiates'),
    )

    channel_of_reference = models.CharField(max_length=15,
                                            choices=CHANNEL,
                                            blank=True,
                                            default='Request',
                                            help_text='Interaction way')

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = RichTextField(help_text="Describe the interaction")

    GRADES = (('-5', '-5'), ('-4', '-4'), ('-3', '-3'), ('-2', '-2'), ('-1', '-1'),
              ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))

    grade = models.CharField(max_length=2,
                             choices=GRADES,
                             blank=True,
                             default='1',
                             help_text='Interaction grade')

    date_of_creation = models.DateField(auto_now_add=True)
    date_of_edition = models.DateField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'Proj.: %s, Comp.: %s' % (self.project, self.company)

    def get_absolute_url(self):
        """
        Returns the url to access a particular interaction instance.
        """
        return reverse('interaction-detail', args=[str(self.id)])

    def get_update_url(self):
        """
        Returns the url to access an updating interaction instance.
        """
        return reverse('interaction-update', args=[str(self.id)])
