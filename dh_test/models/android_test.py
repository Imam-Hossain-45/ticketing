from helpers.models import Model
from django.db import models
from datetime import datetime


class AndroidTestUser(Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='android/test/profile-picture/', null=True, blank=True)
    ticket_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class AndroidTestScanLog(Model):
    ticket_id = models.CharField(max_length=100, blank=True, null=True)
    scan_date = models.DateField()
    scan_time = models.TimeField(default=datetime.time(00,00))
    status = models.CharField(
        max_length=15,
        choices=(
            ('valid', 'Valid'),
            ('invalid', 'Invalid'),
        ),
        default='valid'
    )
