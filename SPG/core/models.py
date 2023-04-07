from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
import uuid
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # user_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
