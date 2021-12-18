from datetime import date

from ckeditor.fields import RichTextField
from django.db import models
from catalog.models import Customer

# Create your models here.
from django.urls import reverse


class Project(models.Model):
    """
    Class defining a model of project.
    """
    title = models.CharField(max_length=300)
    description = RichTextField()
    begin_date = models.DateField(default=date.today, help_text="Project start date")
    end_date = models.DateField(null=True, blank=True, help_text="Project end date")
    price = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Project'

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular project instance.
        """
        return reverse('project-detail', args=[str(self.id)])

    def get_update_url(self):
        """
        Returns the url to update project instance.
        """
        return reverse('project-update', args=[str(self.id)])

    def get_delete_url(self):
        """
        Returns the url to delete project instance.
        """
        return reverse('project-delete', args=[str(self.id)])
