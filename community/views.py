import PIL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from accounts.models import CustomUser
from community.serializers import *
from .models import Channels, Community
from .permission import IsCommunityAdmin
from rest_framework import status

# Create your views here.

class CommunityUserList(APIView):
    #read
    def get(self, request):
        community_set = Community.objects.all()
        serializer = CommunitySerializer(community_set, many=True)
        return Response(serializer.data)

    #create
    def post(self,request):
        serializer = CommunitySerializer(data = request.data)

        if not serializer.is_valid():
            return Response({
                'errors':serializer.errors,
                'message':'Invalid Input, send proper data'
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'message':'Community Created successfully'
        })


class CommunityUserDetail(APIView):    
    #selected object detail
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            return Response({
                'message':"Invalid ID"
            }) 
    
    #read
    def get(self, request, pk):
        community = self.get_object(pk)
        serializer = CommunitySerializer(community)
        return Response(serializer.data)

    #update
    def patch(self, request, pk): 
        community = self.get_object(pk)
        data=request.data
        serializer=CommunitySerializer(community, data=data, partial=True)

        if not serializer.is_valid():
            return Response({
                'errors':serializer.errors
            })

        serializer.save()
        return Response({
            'payload':serializer.data                        
        })        

    #delete/remove
    def delete(self, request, pk):
        try:
            community = self.get_object(pk)
            community.delete()            
            return Response({
                'message':'Community Deleted Successfully'
            })
        except Exception as e:
            return Response({
                'message':'Invalid Id'
            })


class ChannelUserList(APIView):
    #read
    def get(self, request):
        channels = Channels.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)

    #create
    def post(self,request):
        serializer = ChannelSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({
                'errors':serializer.errors,
                'message':'Invalid Input, send proper data'
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'message':'Channel Created successfully'
        })


class ChannelUserDetail(APIView):
    #select object detail
    def get_object(self, pk):
        try:
            return Channels.objects.get(pk=pk)
        except Channels.DoesNotExist:
            return Response({
                'message':'Invalid ID'
            })

    #read
    def get(self, request, pk):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)

    #update
    def patch(self, request, pk):
        channel = self.get_object(pk)
        data=request.data
        serializer = ChannelSerializer(channel, data=data, partial=True)

        if not serializer.is_valid():
            return Response({
                'error':serializer.errors
            })

        serializer.save()
        return Response({
            'payload':serializer.data
        })

    #delete / remove
    def delete(self, request, pk):
        try:
            channel = self.get_object(pk)
            channel.delete()
            return Response({'Channel Deleted Succesfully'})
        except Exception as e:
            return Response({
                'message':'Invalid Id'
            })


class CommunityUserCRUD(APIView):  
    #specific community
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist :
            return Response({
                'errors':'Invalid ID'
            })

    #list of users
    def get(self, request, pk):
        community = self.get_object(pk)
        serializer = CommunityUserSerializer(community)
        return Response({
            'payload':serializer.data
        })

    #adding users
    def post(self,request,pk):
        community = self.get_object(pk)
        add_user = community.users.add(request.data.get('users'))        
        serializer = CommunityUserSerializer(community, data=request.data)

        if not serializer.is_valid():
            return Response({
                'payload':serializer.data,
                'message':'User Added'
            })

        serializer.save()       
        return Response({
            'payload':serializer.data,
            'message':'User added successfully'
        })

    #removing users
    def delete(self, request, pk):
        community = self.get_object(pk)
        delete_user = community.users.remove(request.data.get('users'))
        serializer = CommunityUserSerializer(community, data=request.data)

        data1 = request.data.get('users')
        data_set = Channels.objects.get(pk=community)
        
        if data_set.users.filter(pk=data1).exists():
            data_set.users.remove(data1)
        else :
            pass

        if not serializer.is_valid():
            return Response({
                'payload':serializer.data,
                'message':'User Removed'
            })

        serializer.save()       
        return Response({
            'payload':serializer.data,
            'message':'User removed successfully'
        })


class ChannelUserCRUD(APIView):  

    #specific community
    def get_object(self, pk):
        try:
            return Channels.objects.get(pk=pk)
        except Channels.DoesNotExist :
            return Response({
                'errors':'Invalid ID'
            })

    #list of users
    def get(self, request, pk):
        channel = self.get_object(pk)
        serializer = ChannelUserSerializer(channel)
        return Response({
            'payload':serializer.data
        })

    #adding users

    def post(self,request,pk):

        data1=request.data.get('users')
    #    print(data1)
        channel = self.get_object(pk)
        data_set = channel.community.users.all()
    #    print(data_set)

        channel = self.get_object(pk)

        if channel.community.users.filter(pk=data1).exists():
            add_user = channel.users.add(request.data.get('users'))        
            serializer = ChannelUserSerializer(channel, data=request.data)

            if not serializer.is_valid():
                return Response({
                    'payload':serializer.data,
                    'message':'User Added'
                })

            serializer.save()       
            return Response({
                'payload':serializer.data,
                'message':'User added successfully'
            })

        else :
            return Response({
                'message':'User not present in Community'
            },
            status=status.HTTP_400_BAD_REQUEST)

    #removing users
    def delete(self, request, pk):
        channel = self.get_object(pk)
        delete_user = channel.users.remove(request.data.get('users'))
        serializer = ChannelUserSerializer(channel, data=request.data)

        if not serializer.is_valid():
            return Response({
                'payload':serializer.data,
                'message':'User Removed'
            })

        serializer.save()       
        return Response({
            'payload':serializer.data,
            'message':'User removed successfully'
        })


class CommunityApprove(APIView):

    permission_classes = [IsAdminUser, IsAuthenticated]

    #specific
    def get_object(self,pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            return Response({
                'message':'Invalid ID'
            })

    #sending approval
    def post(self, request, pk):
        community = self.get_object(pk)
        serializer = CommunityApproveSerializer(community, data=request.data)

        if not serializer.is_valid():
            return Response({
                'error':serializer.errors
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'message':'Community Approved'
        })


class ChannelApprove(APIView):

    permission_classes = [IsAuthenticated]

    #specific
    def get_object(self,pk):
        try:
            return Channels.objects.get(pk=pk)
        except Channels.DoesNotExist:
            return Response({
                'message':'Invalid ID'
            })

    #sending approval
    def post(self, request, pk):
        channel = self.get_object(pk)

        if request.user == channel.community.community_admin :    
            serializer = ChannelApproveSerializer(channel, data=request.data)

            if not serializer.is_valid():
                return Response({
                    'error':serializer.errors
                })

            serializer.save()
            return Response({
                'payload':serializer.data,
                'message':'Channel Approved'
           })

        if request.user.is_staff is True:
            serializer = ChannelApproveSerializer(channel, data=request.data)

            if not serializer.is_valid():
                return Response({
                    'error':serializer.errors
                })

            serializer.save()
            return Response({
                'payload':serializer.data,
                'message':'Channel Approved'
           })

        else :
            return Response({
                'message':'Only community admins are allowed to approve Channels',
            },
            status=status.HTTP_400_BAD_REQUEST)


class CommunityChannels(APIView):

    #getting specific community    
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            return Response({
                'message':'Invalid ID'
            })

    #read
    def get(self, request, pk):
        community_object = self.get_object(pk)
        channel_set = Channels.objects.filter(community=community_object)
        serializer = ChannelSerializer(channel_set, many=True)
        return Response(serializer.data)
