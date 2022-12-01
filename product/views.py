from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .import serializers
from .models import*

# Create your views here.

class CategoryCreateListView(generics.GenericAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        caty = Category.objects.all()

        serializer = self.serializer_class(instance=caty, many= True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)   

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.GenericAPIView):
    serializer_class = serializers.CategorySerializer
    #permission_classes=[IsAdminUser]

    def put(self,request, cat_id):
        data = request.data

        caty = get_object_or_404(Category, pk=cat_id)

        serializer = self.serializer_class(data=data,instance=caty)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cat_id):
        caty = get_object_or_404(Category, pk=cat_id)

        caty.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TeaCreateListView(generics.GenericAPIView):
    serializer_class = serializers.TeaSerializer
    queryset = Tea.objects.all()

    def get(self, request):
        tea = Tea.objects.all()

        serializer = self.serializer_class(instance=tea, many= True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)   

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeaDetailView(generics.GenericAPIView):
    serializer_class = serializers.TeaSerializer
    #permission_classes=[IsAdminUser]

    def patch(self,request, tea_id):
        data = request.data

        tea = get_object_or_404(Tea, pk=tea_id)

        serializer = self.serializer_class(data=data,instance=tea)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tea_id):
        tea = get_object_or_404(Category, pk=tea_id)

        tea.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
