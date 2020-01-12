from django.db import models
from helpers.models import Model
from settings.models import GENDER_CHOICES


class VisitorProfile(Model):
    user = models.OneToOneField('user_management.User', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='male'
    )
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user_visitors/profile_pic/', blank=True, null=True)

    def __str__(self):
        return "%s" % self.user
