import uuid
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import models as auth_models
from .manager import UserManager
import PIL
from PIL import Image

# Create your models here.

class CustomUser(auth_models.AbstractUser):
    def nameFile(instance, filename):
        return '/'.join(['userimages',str(instance.name), filename])

    username = None
    email = models.EmailField(unique=True, primary_key=True)
    mobile = models.CharField(max_length=12)
    name = models.CharField(max_length=25)
    DOB = models.DateField()
    profilepic = models.ImageField(upload_to=nameFile, blank=True) 
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