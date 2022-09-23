from django.contrib import admin
from .models import Interests, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Interests)