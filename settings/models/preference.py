from helpers.models import Model
from django.db import models


class Preference(Model):
    caption = models.TextField()

    def __str__(self):
        return "%s" % self.caption
