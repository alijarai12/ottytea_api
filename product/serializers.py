from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'image',
        ]

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = [
            'id',
            'title',
            'description',
            'category',
            'selling_price',
            'old_price',
            'weight',
            'aroma',
            'appearance',
            'vendor',
            'type',
            'product_image',
            'date_created',
        ]
    category = serializers.StringRelatedField()