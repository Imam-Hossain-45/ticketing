from django.contrib import admin
from user_management.models import User, VisitorProfile

# Register your models here.

admin.site.register(User)
admin.site.register(VisitorProfile)
