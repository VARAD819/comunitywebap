from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', ProductAPI.as_view()),
]
