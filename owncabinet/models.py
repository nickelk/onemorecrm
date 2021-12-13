from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class OwnCabinet(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_images/',
                               default='avatar_images/default.jpeg')

    def get_profile_update_url(self):
        """
        Returns the url to update interaction instance.
        """
        return reverse('owncabinet-update', args=[str(self.id)])

    def get_absolute_url(self):
        """
        Returns the url to access a particular profile instance.
        """
        return reverse('owncabinet', args=[str(self.id)])
