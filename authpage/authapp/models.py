# authapp/models.py

# authapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add related_name to avoid clashes
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True, help_text='Specific permissions for this user.')
