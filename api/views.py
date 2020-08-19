from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics , mixins
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from rest_framework.response import Response
from Ecommerce.models import Product 
from django.shortcuts import get_object_or_404
import json
from .serializers import ProductlistSerializers
import Ecommerce


# Creating API Endpoints

# class Productlistview(APIView): # Most basic mehthod of handling get post update data , Better to use the inbuilts provided by djangorestframework
#     permission_classes = []
#     authentication_classes = []

#     def get(self , request , format = False):
#         items = Product.objects.all()
#         serial = ProductlistSerializers(items , many = True)
#         return Response(serial.data)

#     def post(self , request , format = False):
#         pass 


class Productlistview(generics.ListAPIView): # Better method of performing GET requests by showing all the data in the database in the serializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated ]
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            queryset = queryset.filter(desc__icontains = query)

        return queryset


# class Productlistview(mixins.CreateModelMixin,generics.ListAPIView): # Single class handling GET ,POST , DELETE request by inherting Mixins
#     authentication_classes = []
#     permission_classes = []
#     queryset = Product.objects.filter()
#     serializer_class = ProductlistSerializers
#     lookup_field = 'id'

#     def get_object(self , *args , **kwargs):
#         kwargs = self.kwargs
#         q_get = Product.objects.get(id = kwargs['pk'])
#         return q_get

#     def post(self , request , *args , **kwargs):
#         return self.create(request , *args , **kwargs)


class Productview(generics.RetrieveAPIView): #  handling GET request by inherting Mixins for single object 
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    queryset = Product.objects.filter()
    serializer_class = ProductlistSerializers
    lookup_field = 'id'

    def get_object(self , *args , **kwargs):
        print(self.request.user)
        kwargs = self.kwargs
        q_get = Product.objects.get(id = kwargs['pk'])
        return q_get

# class Productview(mixins.DestroyModelMixin,mixins.UpdateModelMixin , generics.RetrieveAPIView): # Single class handling GET and UPDATE request by inherting Mixins for single object 
#                                                                                                 # And so on the classes can be converted to Any combination of CRUD
#     authentication_classes = []
#     permission_classes = []
#     queryset = Product.objects.filter()
#     serializer_class = ProductlistSerializers
#     lookup_field = 'id'

#     def get_object(self , *args , **kwargs):
#         kwargs = self.kwargs
#         q_get = Product.objects.get(id = kwargs['pk'])
#         return q_get

#     def put(self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)

    
#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request , *args , **kwargs)


# class ApiPoint( mixins.CreateModelMixin , 
#                 mixins.RetrieveModelMixin,
#                 mixins.DestroyModelMixin , 
#                 mixins.UpdateModelMixin, 
#                 generics.ListAPIView):  # A single class Performing all CRUD operations

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = ProductlistSerializers

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             queryset = queryset.filter(desc__icontains = query)

#         return queryset

#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id' , None)
#         queryset  = self.get_queryset()
#         obj = None
#         if passed_id != None:
#             obj = get_object_or_404(queryset , id = passed_id)
#             self.check_object_permissions(request , obj)
#         return obj

#     def get(self , request , *args , **kwargs):
#         passed_id = request.GET.get('id')
#         if passed_id is not None:
#             return self.retrieve(request , *args , **kwargs)    
#         return super().get(request , *args , **kwargs)

#     def post(self , request , *args , **kwargs):
#         return self.create(request , *args , **kwargs)

#     def put(self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)

#     def patch(self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)

#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request , *args , **kwargs)



class Createapiview(generics.CreateAPIView): # Basic method of POST request by creating a new data for the database
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializers

class ProductUpdateview(generics.UpdateAPIView): # Basic method of PUT request by updating the data for the database
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializers


class ProductDeleteview(generics.DestroyAPIView): # Basic method of DELETE request by updating the data for the database
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializers


