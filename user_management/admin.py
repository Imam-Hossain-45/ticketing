from django.contrib import admin
from user_management.models import User, UserAuthority, VisitorProfile, BusinessProfile

# Register your models here.

admin.site.register(User)
admin.site.register(UserAuthority)
admin.site.register(VisitorProfile)
admin.site.register(BusinessProfile)
