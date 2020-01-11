from helpers.models import Model
from django.db import models


class Preference(Model):
    caption = models.TextField()
