from django.db import models
from helpers.models import Model


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

LEVEL_CHOICES = (
    ('Best', 'Best'),
    ('Moderate', 'Moderate'),
    ('Normal', 'Normal'),
    ('Worst', 'Worst'),
)


class Country(Model):
    code = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    dial_code = models.CharField(max_length=255, null=True)
    currency = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class UserRegistration(Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male'
    )
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    profile_picture1 = models.ImageField(upload_to='web/test/profile-picture/', blank=True, null=True)
    profile_picture2 = models.ImageField(upload_to='web/test/profile-picture/', blank=True, null=True)

    def __str__(self):
        return self.name


class FnF(Model):
    user_registration = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male'
    )
    mobile_number = models.CharField(max_length=20, blank=True, null=True)


class FoodPreference(Model):
    user_registration = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    food = models.CharField(max_length=200, blank=True, null=True)


class LanguageProficiency(Model):
    user_registration = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        blank=True, null=True
    )
