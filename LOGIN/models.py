from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8, 'Password must have 8 characters')])

    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
