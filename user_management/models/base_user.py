from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError('Users must have a email address')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('visitor', 'Visitor'),
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    email_verified = models.BooleanField(default=False, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone_verified = models.BooleanField(default=False, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    user_type = models.CharField(
        max_length=255,
        choices=USER_TYPE_CHOICES,
        default='admin'
    )
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return "%s" % self.username
