from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class person(models.Model):
    Name        = models.CharField(max_length=60)
    Birth_Year  = models.CharField(max_length=60)
    Eye_Color   = models.CharField(max_length=60)
    Gender      = models.CharField(max_length=60)
    Height      = models.IntegerField()
    def __str__(self):
        return self.Name
