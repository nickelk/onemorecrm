from django.db import models


class Grades(models.IntegerChoices):
    """
    Choises for interaction grades
    """
    FIVE = 5, '5'
    FOUR = 4, '4'
    THREE = 3, '3'
    TWO = 2, '2'
    ONE = 1, '1'
    M_ONE = -1, '-1'
    M_TWO = -2, '-2'
    M_THREE = -3, '-3'
    M_FOUR = -4, '-4'
    M_FIVE = -5, '-5'


class Channel(models.TextChoices):
    """
    Choises for interaction channels
    """
    REQUEST = 'Request', 'Request'
    LETTER = 'Letter', 'Letter'
    WEB_SITE = 'Web site', 'Web site'
    COMP_INIT = 'Company init.', 'Company initiates'
