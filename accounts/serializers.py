from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        token = self.get_token(self.user)
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['mobile'] = self.user.mobile
        return data


class UserSerializer(serializers.ModelSerializer):
    DOB = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
    class Meta:
        model = User
        fields = ['email', 'password', 'mobile', 'name', 'DOB']

    def create(self, validated_data):
        user = User.objects.create(email = validated_data['email'], 
                                   name = validated_data['name'], 
                                   mobile = validated_data['mobile'],
                                   DOB = validated_data['DOB'],
                                   )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    DOB = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
    class Meta:
        model = User
        fields = ['email', 'mobile', 'name', 'DOB','profilepic','is_staff']
        

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'
