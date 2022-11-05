from .views import *
from django.urls import path

urlpatterns = [
path('register/', RegisterUser.as_view()),    
path('interest/', Interest.as_view()),
path('users/', Profile.as_view()),
path('user/<str:pk>',Profile.as_view()),
path('login/', LoginUser.as_view()),
]
