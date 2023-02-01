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
            self.name = f"{self.listing}--{self.date_created}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.listing}------{self.date_created}'


class FullReport(models.Model):
    ACTIONS = (
        ('YES', 'YES'),
        ('YES/TEMPORARY', 'YES/TEMPORARY'),
        ('NO', 'NO'),
        ('N/A', 'N/A'),
        ('NOT CHECKED', 'NOT CHECKED')
    )

    listing = models.ForeignKey(Listing, related_name='fullreports', on_delete=DO_NOTHING, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    file = models.FileField(blank=True, upload_to='reports_files/%Y/%m/%d/', verbose_name="Files", max_length=255) #, storage='reports_files/%Y/%m/%d/')
    # file = models.FilePathField(path=r'C:\Users\ALEXIS\OneDrive\PYTHON-LESSONS\DJANGO-ALL\instruments_project\media\excel_files')
    # file = models.FileField(blank=True)
    output_0_before_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_25_before_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_50_before_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_75_before_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_100_before_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_0_after_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_25_after_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_50_after_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_75_after_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    output_100_after_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manifold_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    ferrules_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    seal_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    mounting_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    cable_gland_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    insulation_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    general_state_correct = models.CharField(max_length=15, choices=ACTIONS, null=True, blank=True)
    comments = models.TextField()

    def save(self, *args, **kwargs):
        # if not self.name:
        self.name = f"{self.listing}--{self.date_created}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.listing}------{self.date_created}'








