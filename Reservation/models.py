from django.db import models
from .choices import PLACE_CHOICES, TIME_CHOICES
from django.utils import timezone
# Create your models here.

class Reservation_Data(models.Model):
    Group1 = models.CharField(max_length=200, blank=False)
    Group2 = models.CharField(max_length=200, blank=False)
    Author = models.CharField(max_length=200, blank=False)
    Place = models.IntegerField(choices=PLACE_CHOICES, default=1, blank=False)
    Time = models.IntegerField(choices=TIME_CHOICES, default=1, blank=False)
    Date = models.DateField(blank=False)

    def __str__(self):
        return self.Author