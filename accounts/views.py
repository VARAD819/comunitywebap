from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Interests, CustomUser
from .serializers import InterestSerializer, ProfileSerializer, UserSerializer 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'errors':serializer.errors})

        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        refresh = RefreshToken.for_user(user)

        return Response({
        'payload' : serializer.data, 
        'refresh': str(refresh), 
        'access': str(refresh.access_token) 
        })


class Interest(APIView):
    def get(self, request):
        interest_set = Interests.objects.all()
        serializer = InterestSerializer(interest_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InterestSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({
                'errors':serializer.errors,
                'message':'Invalid Input'
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'message':'Data added successfully'
        })


class Profile(APIView):
    def get(self, request):
        profile_set = User.objects.all()
        serializer = ProfileSerializer(profile_set, many=True)
        return Response(serializer.data)