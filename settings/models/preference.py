from helpers.models import Model
from django.db import models


class Preference(Model):
    caption = models.TextField()

    def __str__(self):
        return "%s" % self.caption


class UserPreference(Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE, blank=True, null=True)
    preference = models.ForeignKey('settings.Preference', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.preference)
