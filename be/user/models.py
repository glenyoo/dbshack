from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, company_id, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not company_id:
            raise ValueError('The Company ID must be set')

        user = self.model(username=username, company_id=company_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, company_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, company_id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    company_id = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # Login with username
    REQUIRED_FIELDS = ['company_id']  # Required when creating a superuser

    def __str__(self):
        return self.username
