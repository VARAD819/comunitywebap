import PIL
from PIL import Image
import uuid
from uuid import uuid4
from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Community(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images',str(instance.community_name), filename])

    community_admin = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name = 'communityadmin',
        )
    community_name = models.CharField(max_length=250, unique=True)
    community_id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default = uuid.uuid4)
    users = models.ManyToManyField(
        CustomUser,
        related_name = 'communityusers' , 
        blank=True
        )
    approved = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to=nameFile,blank=True)
    icon = models.ImageField(upload_to=nameFile,blank=True)

    def __str__(self):
        return self.community_name   

    class Meta:
        verbose_name_plural="communities"


class Channels(models.Model):
    channel_admin = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name = 'channeladmin',
    )
    channel_id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default = uuid.uuid4)
    channel_name = models.CharField(max_length=250)
    users = models.ManyToManyField(
        CustomUser,
        related_name = 'channelusers' , 
        blank=True
        )
    community = models.ForeignKey(
        Community,
        on_delete = models.CASCADE,
        related_name = 'channelcommunity',
        blank=False,
        null=False,
        to_field = 'community_name'
    )
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.channel_name   

    class Meta:
        verbose_name_plural="channels"
    