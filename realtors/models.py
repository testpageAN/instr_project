from django.db import models
from datetime import datetime


# Create your models here.
class Realtor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50, blank=True)
    is_ours = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
