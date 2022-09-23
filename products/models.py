import uuid
from uuid import uuid4
from django.db import models

# Create your models here.

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
   
    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural = "products"

