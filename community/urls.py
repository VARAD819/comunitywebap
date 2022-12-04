from community.serializers import CommunitySerializer
from .views import *
from django.urls import path

urlpatterns = [
path('', CommunityUserList.as_view()),    
path('<str:pk>',CommunityUserDetail.as_view()),
path('users/<str:pk>',CommunityUserCRUD.as_view()),
path('channels/',ChannelUserList.as_view()),
path('channels/<str:pk>',ChannelUserDetail.as_view()),
path('channels/users/<str:pk>',ChannelUserCRUD.as_view()),
path('approve/<str:pk>',CommunityApprove.as_view()),
path('channels/approve/<str:pk>',ChannelApprove.as_view()),
path('channels/community/<str:pk>',CommunityChannels.as_view()),
path('channels/chats/<str:pk>',ChatChannels.as_view()),
]