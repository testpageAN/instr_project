from django.db import models
from datetime import datetime
from realtors.models import Realtor


# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=50)
    block = models.CharField(max_length=100)
    unit = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=50)
    detailed_type = models.CharField(max_length=100)
    special_type = models.CharField(max_length=100)
    lrv = models.DecimalField(max_digits=10, decimal_places=2)
    urv = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    serial_no = models.CharField(max_length=50, blank=True)
    system_type = models.CharField(max_length=50, blank=True)
    equipment = models.CharField(max_length=50, blank=True)
    project = models.CharField(max_length=100, blank=True)
    interval = models.IntegerField()
    last_checked = models.DateTimeField(default=datetime.now)
    next_check = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    history = models.TextField()
    data_sheet = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.tag