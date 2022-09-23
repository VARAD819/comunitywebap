import uuid
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import models as auth_models
from .manager import UserManager

# Create your models here.
# class UserProfile(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#         ('D', 'Do not want to specify'),
#     )
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, null=True, blank=True)    
#     name = models.CharField(max_length=50,null=True, blank=True)
#     email = models.EmailField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='D')
#     interests = models.ManyToManyField('Interests', blank=True, null=True)
#     is_verified = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

class CustomUser(auth_models.AbstractUser):
    username = None
    email = models.EmailField(unique=True, primary_key=True)
    mobile = models.CharField(max_length=12)
    name = models.CharField(max_length=25)
    DOB = models.DateField()
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    objects = UserManager()

    def __str__(self):
        return self.email


class Interests(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="interests"