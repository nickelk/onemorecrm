from django.db import models
from django.contrib.auth.models import User

from interaction.const import Channel, Grades
from owncabinet.models import OwnCabinet
from django.urls import reverse

from project.models import Project
from ckeditor.fields import RichTextField


# Create your models here.
class Interaction(models.Model):
    """
    Class defining a model of interaction between customer and contractor.
    """
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    channel_of_reference = models.CharField(max_length=15,
                                            choices=Channel.choices,
                                            blank=True,
                                            default='REQUEST',
                                            help_text='Interaction way')
    manager = models.ForeignKey(OwnCabinet, on_delete=models.SET_NULL, null=True)
    description = RichTextField(help_text="Describe the interaction")
    grade = models.IntegerField(choices=Grades.choices,
                                blank=True,
                                default='ONE',
                                help_text='Interaction grade')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_edition = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Interaction'

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.date_of_edition)

    def get_absolute_url(self):
        """
        Returns the url to access a particular interaction instance.
        """
        return reverse('interaction-detail', args=[str(self.id)])

    def get_update_url(self):
        """
        Returns the url to update interaction instance.
        """
        return reverse('interaction-update', args=[str(self.id)])

    def get_delete_url(self):
        """
        Returns the url to delete interaction instance.
        """
        return reverse('interaction-delete', args=[str(self.id)])
