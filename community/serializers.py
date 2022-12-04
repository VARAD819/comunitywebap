from rest_framework import serializers
from .models import *


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommunityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['users']

    def update(self, instance, validated_data):
        instance.users = validated_data.get('users', instance.users)
        instance.save()
        return instance

class ChannelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ['users']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = '__all__'


class CommunityApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['approved']


class ChannelApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ['approved']


class ChatSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField('get_username')

    def get_username(self, chat_object):
        useremail = getattr(chat_object, "user_email")
        username = CustomUser.objects.get(email=useremail).name
        return username

    class Meta:
        model = Chats
        fields = ['message','channel','user_email','user_name','time']