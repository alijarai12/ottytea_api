from django.contrib import admin
from .models import Category, Tea

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'image']

@admin.register(Tea)
class TeaModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'category', 'selling_price', 'old_price', 'weight', 'aroma', 'appearance', 'vendor', 'type', 'product_image']
