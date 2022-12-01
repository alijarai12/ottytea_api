from .models import *
from rest_framework import serializers

class CartCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitem
        fields = ["id", "customer", "tea", "quantity"]        

class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='Pending')
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    class Meta:
        model = Cartitem
        fields=['id','size', 'order_status', 'quantity', 'created_at', 'updated_at']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model = Cartitem
        fields = ['order_status']