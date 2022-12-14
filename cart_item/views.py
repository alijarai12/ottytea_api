from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .import serializers
from .models import*
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CartitemCreateListView(generics.GenericAPIView):
    serializer_class = serializers.CartCreationSerializer
    queryset = Cartitem.objects.all()
    permission_classes=[AllowAny]

    def get(self, request):
        carts = Cartitem.objects.all()

        serializer = self.serializer_class(instance=carts, many= True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # user = request.user
        

        # if serializer.is_valid():
        #     serializer.save(customer=user)

        #return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
