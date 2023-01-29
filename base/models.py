from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)