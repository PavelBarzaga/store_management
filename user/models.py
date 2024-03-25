from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_is_admin = models.BooleanField(default=False)
    user_is_employer = models.BooleanField(default=False)
    user_is_worker = models.BooleanField(default=False)
    user_email = models.EmailField(blank=True, null=True)
