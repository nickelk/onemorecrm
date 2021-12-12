from django.db import models
from django.contrib.auth.models import AbstractUser


class OwnCabinet(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_images/',
                               default='avatar_images/default.jpeg')
