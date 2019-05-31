from django.db import models
from .choices import SUGGEST_CHOICES
from django.utils import timezone
# Create your models here.

class Reservation_Data(models.Model):
    Group1 = models.CharField(max_length=200)
    Group2 = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Reason = models.TextField()
    Place = models.IntegerField(choices=SUGGEST_CHOICES, default=1, blank=True)
    Time = models.DateTimeField

    def __str__(self):
        return self.Author