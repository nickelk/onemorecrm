from typing import Optional

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class OwnCabinet(AbstractUser):
    """
    Class defining a model of user's own cabinet.
    """
    avatar = models.ImageField(upload_to='avatar_images/',
                               default='avatar_images/default.jpeg')

    class Meta:
        ordering = ['id']
        verbose_name = 'Custom user profile'

    def get_absolute_url(self) -> Optional[str]:
        """
        Returns the url to access a particular profile instance.
        """
        return reverse('owncabinet')
