from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerailizers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductAPI(APIView):
    authentication_classes= [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        product_set = Products.objects.all()
        serializer = ProductSerailizers(product_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerailizers(data = request.data)

        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors,
                'message': 'Invalid data provided'
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'messaage':'Data added successfully'
        })

    def patch(self, request):
        try :
            product = Products.objects.get(id=request.data['id']) 

            serializer = ProductSerailizers(product, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'errors':serializer.errors,
                    'message': 'Invalid input'
                })

            serializer.save()
            return Response({
                'payload': serializer.data,
                'message':'Data Updated'
            })
        
        except Exception as e:
            print(e)
            return Response({
                'message':'Invalid Data'
            })

    def delete(self, request):
        try:
            id = request.GET.get('id')
            product = Products.objects.get(id = id)
            product.delete()
            return Response({
                'message':'Deleted'
            })
        except Exception as e:
            return Response({
                'message':'Invalid Id'
            })
