from django.db import models
from helpers.models import Model

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class VisitorProfile(Model):
    user = models.OneToOneField('user_management.User', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=255,
        choices=GENDER_CHOICES,
        default='male'
    )
    date_of_birth = models.DateField(blank=True, null=True)
