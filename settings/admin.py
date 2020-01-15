from django.contrib import admin
from settings.models import Address, Preference, UserPreference

# Register your models here.

admin.site.register(Address)
admin.site.register(Preference)
admin.site.register(UserPreference)

