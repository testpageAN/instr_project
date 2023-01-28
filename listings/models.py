from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime
from django.utils import timezone

from django.db.models import ForeignKey, DO_NOTHING
from django.core.exceptions import ValidationError
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
    next_check = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    history = models.TextField()
    data_sheet = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    # file = ArrayField(models.FileField(upload_to='reports_files/%Y/%m/%d/', null=True, blank=True), null=True, blank=True)

    def __str__(self):
        return self.tag


class Report(models.Model):
    listing = models.ForeignKey(Listing, related_name='reports', on_delete=DO_NOTHING, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    file = models.FileField(blank=True, upload_to='reports_files/%Y/%m/%d/', verbose_name="Files")#, validators=[validate_file_size], help_text="Allowed size is 5MB")

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.date_created
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.date_created}'








